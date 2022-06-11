from doctest import master
from traceback import format_exc
import xmlrpc.client

master = xmlrpc.client.ServerProxy('http://localhost:9000')
workers = []
aux = 0

while (aux != -1):
    print('\n1. List Workers')
    print('2. Apply A Function Along An Axis Of The DataFrame')
    print('3. Read Columns Labels')
    print('4. Group DataFrame Using A Mapper Or By A Series Of Columns')
    print('5. Read X Number Of Rows')
    print('6. Check Whether Each Element In The DataFrame Is Contained In Values')
    print('7. Iterate Over The DataFrame Columns')
    print('8. Get The Maximum Of The Values Over The Requested Column')
    print('9. Get The Minimum Of The Values Over The Requested Column.')
    print('10. Exit\n')
    num = int(input("Choose an option: "))

    match num:
        case 1:
            result = master.listWorker()
            for address in result:
                workers.append(xmlrpc.client.ServerProxy(address))
        case 2:
            func = input("Function To Apply Required: ")
            print("hola")
        case 3: 
            nameFile = input("Name File Required: ")
            print("hola")
        case 4:
            by = input("Mapping, Function, Label Or List Of Labels Is Required")
            nameFile = input("Name File Required: ")
            print("hola")
        case 5:
            numRows = input("Number Of Rows Required: ")
            nameFile = input("Name File Required: ")
            print("hola")
        case 6:
            values = input("Values Required (Iterable, Series, DataFrame Or Dict): ")
            nameFile = input("Name File Required: ")
            print("hola")
        case 7:
            nameFile = input("Name File Required: ")
            print("hola")
        case 8:
            label = input("Column Label Reuqired: ")
            nameFile = input("Name File Required: ")
            print("hola")
        case 9:
            label = input("Column Label Reuqired: ")
            nameFile = input("Name File Required: ")
            print("hola")
        case 10:
            aux = -1
            result = "Have A Nice Day!"

    print(result)