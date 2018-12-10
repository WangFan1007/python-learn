
import os
import time

from multiprocessing import Process


def func():
    print(12345)
    print('子进程id:'+ str(os.getpid()))
    print("ooid" + str(os.getppid()))
    time.sleep(3)

p = Process(target=func)

p.start()
print('父进程ID：'+str(os.getpid()))
