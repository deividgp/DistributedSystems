import logging
import os
import redis
import time
import sys
from redis.client import Redis
from xmlrpc.server import SimpleXMLRPCServer
from multiprocessing import Process

WORKERS = {}
WORKER_ID = 0
llista = {}
cua = 'cua_jobs' 
r = None

def startWorker(w_id):
    global cua
    global r
    
    while True:
        elem = r.lpop(cua)

        if elem != None:
            line = str(elem).split(':')
            task = line[0]
            task = task[2:]
        
            fitxer = line[1]
            fitxer = fitxer[:len(fitxer)]
            
            cont = line[2]
            cont = cont[2:len(cont)-1]

            num = line[3]
            num =  num[:len(num)-1]

            url = 'http://localhost:8000/' + fitxer
            os.system('curl ' + url + '> redireccio_'+ cont + num + '.txt')
            arg1 = 'redireccio_' + cont + num + '.txt'
            
            result = eval(task)(arg1)
            if (int(num) > 0):
                time.sleep(1)

                aux = r.get(cont)
                aux = str(aux)
                aux = aux[2:len(aux)-1]  
                
                result = aux + '*' + str(result)

            r.mset({cont : str(result)})
            os.system('rm ' + arg1)

def createWorker():
    global WORKERS
    global WORKER_ID

    proces = Process(target=startWorker, args=(WORKER_ID,))
    proces.start()
    
    WORKERS[WORKER_ID] = proces
    WORKER_ID =  WORKER_ID+1
    return ('WORKER CREAT = ',WORKER_ID)



if __name__ == '__main__':
        
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    server = SimpleXMLRPCServer(
       ('localhost', 9000),
        logRequests=True,
       )

    server.register_function(createWorker)
    server.register_function(deleteWorker)
    server.register_function(listWorker)
    server.register_function(countingWords)
    server.register_function(wordCount)
    server.register_function(tractar_cua)
    server.register_function(getResult)
    
    r = redis.Redis()
    r.set("counter", 0)

    # Start the server
    try:
        print('Control+C PER SURTIR')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')