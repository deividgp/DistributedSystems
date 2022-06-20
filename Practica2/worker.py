from concurrent.futures import thread
import logging
from typing import final
from unittest import result
import pandas
import sys
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import numpy
import threading
import time
import redis
import json
import socket
import random

# First Redis handler which receives an updated workers list from the master


def hnd(msg):
    global workers

    if ownMaster == False:
        workers = json.loads(msg["data"])
        print(workers)

# Second Redis handler which receives the new pingMasterAddress


def hnd2(msg):
    global pingMasterAddress
    if ownMaster == False:
        pingMasterAddress = msg["data"]

# Check if port is active


def checkPort(port):
    result = True
    try:
        s = socket.socket()
        s.connect(("localhost", port))
        s.close()
    except:
        result = False
    return result


def pingThread(stop_event):
    global ownMaster, pingMasterAddress, workers

    while not stop_event.is_set():
        # Auxiliar list that stores worker addresses
        auxWorkers = workers
        # If there is just one worker or the pingMasterAddress corresponds to the worker own address
        if len(auxWorkers) == 1 or pingMasterAddress == address:
            if checkPort(9000) == False:
                # Waits for task to end
                while inTask:
                    time.sleep(0.25)
                # Shuts down the current worker server
                server.shutdown()
                server.server_close()
                ownMaster = True
            if len(auxWorkers) > 1:
                red.publish("nextWorker", random.choice(
                    [x for x in auxWorkers if x != address]))
            # If only one worker left 
            elif len(auxWorkers) == 1:
                pingMasterAddress = address

        # If the worker turns into a master then the loop ends
        if ownMaster:
            break
        
        # Iterate through the workers list
        for worker in auxWorkers:
            if worker != address:
                # Get the port from the address
                port = worker.split(":")[2]
                # If not active
                if checkPort(int(port)) == False:
                    # Remove the worker
                    aux = master.deleteWorker(worker)
                    if worker == pingMasterAddress and aux:
                        # Chooses a new pingMasterAddress among all workers but the inactive one
                        red.publish("nextWorker", random.choice(
                            [x for x in auxWorkers if x != worker]))
        time.sleep(0.5)

# Worker functions
def read_csv(route):
    global df
    df = pandas.read_csv(route)


def apply(func, label):
    global inTask
    inTask = True
    result = df[label].apply(eval(func)).values.tolist()
    inTask = False
    return result


def columns():
    global inTask
    inTask = True
    result = df.columns.values.tolist()
    inTask = False
    return result


def groupby(label, op):
    global inTask
    inTask = True
    if (op == "mean"):
        result = df.groupby(label).mean()
    else:
        result = df.groupby(label).sum()
    inTask = False
    return result.to_csv()


def head(num):
    global inTask
    inTask = True
    result = df.head(num).values.tolist()
    inTask = False
    return result


def isin(val1, val2, label):
    global inTask
    inTask = True
    result = df[label].isin([(val1), (val2)]).values.tolist()
    inTask = False
    return result


def items(label):
    global inTask
    inTask = True
    result = []
    for label, content in df[label].items():
        if (type(content) is not str):
            result.append((label, str(content)))
        else:
            result.append((label, content))
    inTask = False
    return result


def max(label):
    global inTask
    inTask = True
    result = df[label].max()
    if (type(result) is not str):
        result = result.item()
    inTask = False
    return result


def min(label):
    global inTask
    inTask = True
    result = df[label].min()
    if (type(result) is not str):
        result = result.item()
    inTask = False
    return result

# Master functions


def addWorker(address):
    if address != "http://localhost:9000" and address not in workers:
        workers.append(address)
        red.publish("workers", json.dumps(workers))
        print(workers)
        return True
    return False


def getWorkers():
    return workers


def deleteWorker(address):
    if address in workers:
        workers.remove(address)
        red.publish("workers", json.dumps(workers))
        print(workers)
        return True
    return False


pingMasterAddress = ""
df = ""
workers = []
inTask = False
ownMaster = False
created = False
address = "http://localhost:"+sys.argv[1]

try:
    # Redis initialization to get data as soon as possible
    red = redis.Redis('localhost', 6379, charset="utf-8",
                      decode_responses=True)
    p = red.pubsub()
    p.subscribe(**{'workers': hnd, 'nextWorker': hnd2})
    x = p.run_in_thread(sleep_time=0.001)

    logging.basicConfig(level=logging.INFO)

    server = SimpleXMLRPCServer(
        ('localhost', int(sys.argv[1])),
        logRequests=True,
        allow_none=True
    )

    server.register_function(apply)
    server.register_function(columns)
    server.register_function(groupby)
    server.register_function(head)
    server.register_function(isin)
    server.register_function(items)
    server.register_function(max)
    server.register_function(min)

    route = input("CSV route: ")

    # read_csv(route)
    master = xmlrpc.client.ServerProxy('http://localhost:9000')
    created = master.addWorker(address)

    if created:
        workers = master.getWorkers()
        if len(workers) == 1:
            pingMasterAddress = address

        stop_event = threading.Event()
        t = threading.Thread(
            daemon=True, target=pingThread, args=(stop_event,))
        t.start()
        print('Control+C PER SORTIR')

        server.serve_forever()
        ownMaster = True
        server = SimpleXMLRPCServer(
            ('localhost', 9000),
            logRequests=True,
            allow_none=True
        )

        server.register_function(addWorker)
        server.register_function(getWorkers)
        server.register_function(deleteWorker)

        if len(workers) == 1:
            deleteWorker(address)

        stop_event.set()
        t.join()
        x.stop()
        p.unsubscribe()
        print("I AM MASTER NOW")
        server.serve_forever()
    else:
        print("worker with address " + address+" could not be created")

except KeyboardInterrupt:
    print('Exiting')
finally:
    if ownMaster == False and created and len(workers) == 1:
        master.deleteWorker(address)
    stop_event.set()
    x.stop()
