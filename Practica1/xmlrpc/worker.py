from audioop import add
from doctest import master
import logging
import os
import pandas
import sys
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

df = ""

def read_csv(route):
    global df
    df = pandas.read_csv(route)

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

address = "http://localhost:"+sys.argv[1]

logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(
    ('localhost', int(sys.argv[1])),
    logRequests=True,
)

master = xmlrpc.client.ServerProxy('http://localhost:9000')

master.createWorker(address)

#server.register_function(read_csv)
server.register_function(apply)
server.register_function(columns)
server.register_function(groupby)
server.register_function(head)
server.register_function(isin)
server.register_function(items)
server.register_function(max)
server.register_function(min)

print("CSV route:")
route = input()
read_csv(route)

try:
    print('Control+C PER SORTIR')
    server.serve_forever()
except KeyboardInterrupt:
    master.deleteWorker(address)
    print('Exiting')
    