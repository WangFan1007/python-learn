from multiprocessing import Pool


def func1(n):
    return n+1

def func2(m):
    print(m)


if __name__ == '__main__':
    p = Pool()

    p.apply_async(func1,args=(10,),callback=func2)
    p.close()
    p.join()