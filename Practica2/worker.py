import logging
import pandas
import sys
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import numpy

df = ""


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


address = "http://localhost:"+sys.argv[1]

logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(
    ('localhost', int(sys.argv[1])),
    logRequests=True,
    allow_none=True
)

master = xmlrpc.client.ServerProxy('http://localhost:9000')

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

created = master.createWorker(address)

if created:
    try:
        print('Control+C PER SORTIR')
        server.serve_forever()
    except KeyboardInterrupt:
        master.deleteWorker(address)
        print('Exiting')
else:
    print("worker with address " + address+" could not be created")
