import redis
import string
import random


def generateListName():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)
num = 0

while (num != 9):
    print('\n1. Apply A Function Along An Axis Of The DataFrame')
    print('2. Read Columns Labels')
    print('3. Group DataFrame Using A Mapper Or By A Series Of Columns')
    print('4. Read X Number Of Rows')
    print('5. Check Whether Each Element In The DataFrame Is Contained In Values')
    print('6. Iterate Over The DataFrame Columns')
    print('7. Get The Maximum Of The Values Over The Requested Column')
    print('8. Get The Minimum Of The Values Over The Requested Column.')
    print('9. Exit\n')
    num = int(input("Choose an option: "))

    result = ""
    params = ""
    if num != 9:
        listName = generateListName()

    match num:
        case 1:
            func = input("Function To Apply Required: ")
            
            red.publish("functions", "apply:"+listName+":"+params)
        case 2:
            nameFile = input("Name File Required: ")
            red.publish("functions", "columns:"+listName+":"+params)
        case 3:
            by = input("Mapping, Function, Label Or List Of Labels Is Required")
            nameFile = input("Name File Required: ")
            red.publish("functions", "groupby:"+listName+":"+params)
        case 4:
            numRows = input("Number Of Rows Required: ")
            nameFile = input("Name File Required: ")
            red.publish("functions", "head:"+listName+":"+params)
        case 5:
            values = input(
                "Values Required (Iterable, Series, DataFrame Or Dict): ")
            nameFile = input("Name File Required: ")
            red.publish("functions", "isin:"+listName+":"+params)
        case 6:
            nameFile = input("Name File Required: ")
            red.publish("functions", "items:"+listName+":"+params)
        case 7:
            label = input("Column Label Reuqired: ")
            nameFile = input("Name File Required: ")
            red.publish("functions", "max:"+listName+":"+params)
        case 8:
            label = input("Column Label Reuqired: ")
            nameFile = input("Name File Required: ")
            red.publish("functions", "min:"+listName+":"+params)
        case 9:
            result = "Have A Nice Day!"

    print(result)
