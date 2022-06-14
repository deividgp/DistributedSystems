import logging
import re
import redis
import pandas
import numpy

df = ""


def read_csv(route):
    global df
    df = pandas.read_csv(route)


def apply(queue, params):
    result =  df[params[1]].apply(eval(params[0])).to_csv()
    red.rpush(queue, result)


def columns(queue, params):
    results = df.columns
    finalResult = ""
    for result in results:
        finalResult = finalResult + result + ", "
    red.rpush(queue, finalResult)


def groupby(queue, params):
    if (params[1] == "mean"):
        results = df.groupby(params[0]).mean()
    else:
        results = df.groupby(params[0]).sum()
    red.rpush(queue, results.to_csv())


def head(queue, params):
    results = []
    results = df.head(int(params[0]))
    red.rpush(queue, results.to_csv())


def isin(queue, params):
    results = []
    print(params)
    results = df[params[2]].isin([(params[0]), (params[1])])
    red.rpush(queue, results.to_csv())

def items(queue, params):
    results = []
    for label, content in df[params[0]].items():
        if (type(content) is not str):
            results.append((label, str(content)))
        else:
            results.append((label, content))
    finalResult = ""
    for result in results:       
        finalResult = finalResult +  ','.join(str(s) for s in result) + "\n"
    red.rpush(queue, finalResult)


def max(queue, params):
    aux = df[params[0]].max()
    result = ""
    if (type(aux) is not str):
        result =  aux.item()
    else:
        result = aux
    red.rpush(queue, result)

def min(queue, params):
    aux = df[params[0]].min()
    result = ""
    if (type(aux) is not str):
        result = aux.item()
    else:
        result = aux
    red.rpush(queue, result)

red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)

logging.basicConfig(level=logging.INFO)

print("CSV route:")
route = input()
read_csv(route)

sub = red.pubsub()
sub.subscribe("functions")

while True:
    message = sub.get_message()
    if message and message["data"] != 1:
        func, queue, params = message["data"].split(":")
        eval(func)(queue, params.split(","))
        print(message)
