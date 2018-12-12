from gevent import monkey;monkey.patch_all()

import time
import gevent

def task():
    time.sleep(1)
    print(12345)

def sync():
    for i in range(10):
        task()

def a_sync():
    g_list = []
    for i in range(10):
        t = gevent.spawn(task)
        g_list.append(t)
    # for tsk in g_list: tsk.join()
    gevent.joinall(g_list)


sync()
a_sync()
