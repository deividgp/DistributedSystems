import logging
from xmlrpc.server import SimpleXMLRPCServer

workers = []

def createWorker(address):
    workers.append(address)
    print(workers)
    
def listWorkers():
    return workers

def deleteWorker(address):
    workers.remove(address)
    print(workers)

logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True,
    allow_none=True
)

server.register_function(createWorker)
server.register_function(listWorkers)
server.register_function(deleteWorker)

try:
    print('Control+C PER SORTIR')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')