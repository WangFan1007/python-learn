
def consumer():
    while True:
        x = yield
        print('consumer处理了任务',x)


def producer():
    c = consumer()
    next(c)

    for i in range(10):
        print('生产了数据:',i)
        c.send(i)


producer()
