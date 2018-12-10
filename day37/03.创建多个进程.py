import time
from multiprocessing import Process

def func(arg0,arg1):
    print('*' * arg0)
    time.sleep(2)
    print('*' * arg1)


p_list = []
for i in range(5):
    p = Process(target=func,args=(2,3))
    p.start()
    p_list.append(p)
    # p.join() #这里所有的都变成同步了

[p.join() for p in p_list] #这是在需要的时候同步
print("执行完了")