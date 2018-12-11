

# e = Event()
#
# print(e.is_set())
#
# e.set()
# e.clear()
# e.wait()
#红绿灯事件

import time
import random
from multiprocessing import Event,Process

def light(e):
    while True:
        if e.is_set():
            print('\033[32m绿灯亮了\033[0m')
            time.sleep(2)
            e.clear()
        else:
            print('\033[31m红灯亮了\033[0m')
            time.sleep(2)
            e.set()


def cars(e,i):
    if not e.is_set():
        print('car %i在等待通行'%i)
        e.wait()
    print('car %i通过了'%i)



if __name__ == '__main__':
    e = Event()
    traffic = Process(target=light,args=(e,))
    traffic.start()

    for i in range(20):
        car = Process(target=cars,args=(e,i))
        car.start()
        time.sleep(random.random())

