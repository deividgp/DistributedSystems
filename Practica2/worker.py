from concurrent.futures import thread
import logging
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


def hnd(msg):
    global workers
    workers = json.loads(msg["data"])
    workers.append("http://localhost:9000")
    print(workers)


def pingThread(stop_event):
    while not stop_event.is_set():
        for worker in workers:
            time.sleep(5)
            if worker == "http://localhost:9000":
                port = worker.split(":")[2]
                try:
                    s = socket.socket()
                    s.connect(("localhost", int(port)))
                    s.close()
                except:
                    
                    print("no es pot connectar")
            elif worker != address:
                port = worker.split(":")[2]
                try:
                    s = socket.socket()
                    s.connect(("localhost", int(port)))
                    s.close()
                    print("es pot connectar")
                except:
                    master.deleteWorker(worker)
                    print("no es pot connectar")


def read_csv(route):
    global df
    df = pandas.read_csv(route)


def apply(func, label):
    return df[label].apply(eval(func)).values.tolist()


def columns():
    results = df.columns
    return results.values.tolist()


def groupby(label, op):
    if (op == "mean"):
        results = df.groupby(label).mean()
    else:
        results = df.groupby(label).sum()
    return results.to_csv()


def head(num):
    return df.head(num).values.tolist()


def isin(val1, val2, label):
    return df[label].isin([(val1), (val2)]).values.tolist()


def items(label):
    result = []
    for label, content in df[label].items():
        if (type(content) is not str):
            result.append((label, str(content)))
        else:
            result.append((label, content))
    return result


def max(label):
    aux = df[label].max()
    if (type(aux) is not str):
        return aux.item()
    else:
        return aux


def min(label):
    aux = df[label].min()
    if (type(aux) is not str):
        return aux.item()
    else:
        return aux

def newMaster():
    print("hola")

def masterChosen():
    print("hola")

master = xmlrpc.client.ServerProxy('http://localhost:9000')

df = ""
workers = []

address = "http://localhost:"+sys.argv[1]

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

created = master.addWorker(address)

if created:
    try:
        workers = master.getWorkers()
        red = redis.Redis('localhost', 6379, charset="utf-8",
                          decode_responses=True)
        p = red.pubsub()
        p.subscribe(**{'workers': hnd})
        x = p.run_in_thread(sleep_time=0.001)
        stop_event = threading.Event()
        t = threading.Thread(
            daemon=True, target=pingThread, args=(stop_event,))
        t.start()
        print('Control+C PER SORTIR')
        server.serve_forever()
    except KeyboardInterrupt:
        stop_event.set()
        master.deleteWorker(address)
        x.stop()
        print('Exiting')
else:
    print("worker with address " + address+" could not be created")
