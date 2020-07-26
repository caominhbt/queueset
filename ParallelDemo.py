import multiprocessing as mp
from multiprocessing import Queue
from QueueSet import QueueSet
from random import random

def process1(qset, value):
    while True:
        print("Process 1: Running...............")
        for i in range(1000):
            nvalue = value + str(i)
            print("######New Value Is: ",nvalue )
            qset.put_data(nvalue)


def process2(qset, qset2):
    while True:
        print("Process 2: Running...........")
        qvalue = qset.get_data()
        qset2.put_data(qvalue)
        print("$$$$$$$$$Value in Queue: ", qvalue)


def process3(qset2):
    while True:
        print("Process 3: Running............")
        print("********Value in Queue of process 3: ", qset2.get_data())
        #a = 1 + 2

if __name__ == "__main__":
    #q = Queue()
    print("Starting")
   # cores = mp.cpu_count()
    #print(cores)
    #pool = mp.Pool(cores)

    #pool.apply(process1, args=(q, 'Minh',))
    #pool.apply(process2, args=(q,))

    #pool.close()
   # pool.join()

    qset = QueueSet(3)
    qset2 = QueueSet(3)
    processes = []
    p1 = mp.Process(target=process1, args=(qset, 'v-'))
    processes.append(p1)
    p2 = mp.Process(target=process2, args=(qset, qset2))
    processes.append(p2)

    p3 = mp.Process(target=process3, args=(qset2,))
    processes.append(p3)

    for p in processes:
        p.start()