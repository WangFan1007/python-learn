from multiprocessing import Pool

def func(n):
    print(n)

if __name__ == '__main__':
    pool = Pool(5)
    pool.map(func,range(100))