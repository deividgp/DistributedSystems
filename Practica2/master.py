import logging
from xmlrpc.server import SimpleXMLRPCServer
import redis
import json
import time

workers = []

def createWorker(address):
    if address != "9000" and address not in workers:
        workers.append(address)
        red.publish("workers", json.dumps(workers))
        print(workers)
        return True
    return False

    
def listWorkers():
    return workers

def deleteWorker(address):
    workers.remove(address)
    print(workers)

red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)

logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True,
    allow_none=True
)

createWorker("55454")

server.register_function(createWorker)
server.register_function(listWorkers)
server.register_function(deleteWorker)

try:
    print('Control+C PER SORTIR')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')