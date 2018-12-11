
import time
from multiprocessing import Pool

def func(i):
    time.sleep(0.5)
    return i*i




if __name__ == '__main__':

    p = Pool(5)
    res_list = []
    for i in range(10):
        res = p.apply_async(func,args=(i,))
        # print(res.get()) #get 阻塞等待结果
        res_list.append(res)

    for res in res_list :
        print(res.get())