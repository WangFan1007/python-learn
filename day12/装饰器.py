

def wrapper(func):
    def inner(*args, **kwargs):
        print('before exec')
        ret = func(*args, **kwargs)
        print('end exec')
        return ret
    return inner

@wrapper
def test(a,b):
    print(a + b)

test(10,20)