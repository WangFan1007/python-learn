


import time
import random
from multiprocessing import JoinableQueue,Process

def consunmer(name,q):
    while True:
        time.sleep(random.randint(0, 2))
        foods = q.get()
        print('%s消费了%s'%(name,foods))
        q.task_done()


def producer(name,food,q):
    for i in range(4):
        time.sleep(random.randint(0,2))
        foods = '%s生产了%s%s'%(name,food,i)
        print(foods)
        q.put(foods)
    q.join()


if __name__ == '__main__':
    q = JoinableQueue(20)

    p1 = Process(target=producer,args=('egon','包子',q))
    p1.start()

    p2 = Process(target=producer, args=('jason', '包子', q))
    p2.start()

    c = Process(target=consunmer,args=('alise',q))
    c.daemon = True
    c.start()
    c2 = Process(target=consunmer,args=('hanke',q))
    c2.daemon = True
    c2.start()

    p1.join()
    p2.join()
