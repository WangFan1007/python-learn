

def wrapper(func):
    def inner(*args, **kwargs):
        print('before exec')
        func(*args, **kwargs)
        print('end exec')
    return inner

@wrapper
def test(a,b):
    print(a + b)

test(10,20)