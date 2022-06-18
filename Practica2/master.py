import logging
from xmlrpc.server import SimpleXMLRPCServer
import redis
import json
import time
import subprocess

#subprocess.call("coordinator.py", shell=True)

workers = []

def findWorker():
    

def addWorker(address):
    if address != "http://localhost:9000" and address not in workers:
        workers.append((address,False))
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


def updateWorker(address, busy):
    print("hola")

red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)

logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True,
    allow_none=True
)

server.register_function(addWorker)
server.register_function(getWorkers)
server.register_function(deleteWorker)

try:
    print('Control+C PER SORTIR')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
