
import os
import time
from threading import Thread,Lock

def func():

    # print(n,os.getpid())
    l.acquire()
    global g
    temp = g
    time.sleep(0.2) #这里是强制切换CPU
    g = temp - 1
    l.release()

g = 100
print('主线程',os.getpid())
t_list = []
print(g)
l = Lock()

for i in range(10):
    t = Thread(target=func)
    t_list.append(t)
    t.start()

for th in t_list: th.join()
print(g)