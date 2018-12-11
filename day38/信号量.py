
import time
import random

from multiprocessing import Process
from multiprocessing import Semaphore


def ktv(i,sem):
    sem.acquire()
    print('%s走进ktv'%i)
    time.sleep(random.randint(1,5))
    print('%s走出ktv' % i)
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(4)
    for i in range(20):
        p = Process(target=ktv,args=(i,sem))
        p.start()