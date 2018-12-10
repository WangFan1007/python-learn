
import time
from multiprocessing import Process

def func():
    while True:
        print("我还活着")
        time.sleep(0.5)

# 守护进程随着 主进程的代码执行完毕而结束
def func2():
    print("子任务开始")
    time.sleep(8)
    print("子任务结束")

p = Process(target=func)
p.daemon = True
p.start()

Process(target=func2).start()


for i in range(5):
    print("主进程")
    time.sleep(1)


print("主进程结束")