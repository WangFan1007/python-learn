
import time
from concurrent.futures import ThreadPoolExecutor


def func(n):
    time.sleep(0.5)
    # print(n)
    return n*n

def call_back(m):
    print('结果是 %s'%m.result())

tpool = ThreadPoolExecutor()

# t.submit(func,2)
t_list = []
for i in range(20):
    task = tpool.submit(func,i)
    task.add_done_callback(call_back)
    t_list.append(task)


# tpool.shutdown()
# print('主线程')
for t in t_list: print(t.result())