import logging
import os
import pandas
import time
import sys
import datetime
from xmlrpc.server import SimpleXMLRPCServer
from multiprocessing import Process

WORKERS = {}
WORKER_ID = 0
llista = {}
cua = 'cua_jobs' 

def createWorker():
    global WORKER_ID

    WORKER_ID =  WORKER_ID+1
    return ('WORKER CREAT = ',WORKER_ID)

def deleteWorker(cont):
    global WORKERS
    global WORKER_ID
    
    proces = WORKERS[cont-1]
    proces.terminate()
    proces.is_alive()
    WORKERS.pop(cont-1)
    
    return ('WORKER ELIMINAT= ',cont)

def read_csv():
    print("hola")

def apply():
    print("hola")

def columns():
    print("hola")

def groupby():
    print("hola")

def head():
    print("hola")

def isin():
    print("hola")

def items():
    print("hola")

def apply():
    print("hola")

def max():
    print("hola")

def min():
    print("hola")

if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    server = SimpleXMLRPCServer(
       ('localhost', 9000),
        logRequests=True,
       )

    server.register_function(createWorker)

    # Start the server
    try:
        print('Control+C PER SURTIR')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')