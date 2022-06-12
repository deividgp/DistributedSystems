import logging
import redis
import pandas

df = ""


def read_csv(route):
    global df
    df = pandas.read_csv(route)


def apply(queue, params):
    return df[label].apply(eval(func)).values.tolist()


def columns(queue, params):
    results = df.columns
    return results.values.tolist()


def groupby(queue, params):
    if (op == "mean"):
        results = df.groupby(label).mean()
    else:
        results = df.groupby(label).sum()
    return results.to_csv()


def head(queue, params):
    return df.head(num).values.tolist()


def isin(queue, params):
    return df[label].isin([(val1), (val2)]).values.tolist()


def items(queue, params):
    result = []
    for label, content in df[label].items():
        if (type(content) is not str):
            result.append((label, str(content)))
        else:
            result.append((label, content))
    return result


def max(queue, params):
    aux = df[label].max()
    if (type(aux) is not str):
        return aux.item()
    else:
        return aux


def min(queue, params):
    aux = df[label].min()
    if (type(aux) is not str):
        return aux.item()
    else:
        return aux


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
        eval(func)(queue, params.split(","))
        print(message)
