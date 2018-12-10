from multiprocessing import Process
import os

class MyProcess(Process):
    def __init__(self,arg1,arg2):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
    def run(self):
        print('子id:',os.getpid())


print('主id:',os.getpid())
p = MyProcess(3,4)
p.start()
p2 = MyProcess(4,5)
p2.start()