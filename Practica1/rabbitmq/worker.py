import logging
import pika
import pandas

df = ""


def read_csv(route):
    global df
    df = pandas.read_csv(route)


def apply(queue, params):
    print("hola")


def columns(queue, params):
    print("hola")


def groupby(queue, params):
    print("hola")


def head(queue, params):
    print("hola")


def isin(queue, params):
    print("hola")


def items(queue, params):
    print("hola")


def max(queue, params):
    print("hola")


def min(queue, params):
    print("hola")


red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)

logging.basicConfig(level=logging.INFO)

print("CSV route:")
route = input()
# read_csv(route)

sub = red.pubsub()
sub.subscribe("functions")

while True:
    message = sub.get_message()
    if message and message["data"] != 1:
        func, queue, params = message["data"].split(":")
        eval(func)(queue, params)
        print(message)
