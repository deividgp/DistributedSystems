from audioop import add
import logging
import os
from time import process_time_ns
from unittest import result
import pandas
import sys
from xmlrpc.server import SimpleXMLRPCServer
import redis

df = ""


def read_csv(route):
    global df
    df = pandas.read_csv(route)


def apply():
    print("hola")


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


def isin(val1, val2):
    print(df.isin([val1, val2]))
    return df.isin([val1, val2]).values.tolist()


def items():
    print("hola")


def max():
    print("hola")


def min():
    print("hola")

red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)

address = "http://localhost:"+sys.argv[1]

logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(
    ('localhost', int(sys.argv[1])),
    logRequests=True,
    allow_none=True
)

red.sadd("workers", address)

# server.register_function(read_csv)
server.register_function(apply)
server.register_function(columns)
server.register_function(groupby)
server.register_function(head)
server.register_function(isin)
server.register_function(items)
server.register_function(max)
server.register_function(min)

route = input("CSV route:")
#read_csv(route)

try:
    print('Control+C PER SORTIR')
    server.serve_forever()
except KeyboardInterrupt:
    red.srem("workers", address)
    print('Exiting')
