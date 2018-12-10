import time
from multiprocessing import Process

def func(arg0,arg1):
    print('*' * arg0)
    time.sleep(2)
    print('*' * arg1)


p = Process(target=func,args=(4,5))
p.start()
print('hahahah')
p.join()
print('====运行完了')