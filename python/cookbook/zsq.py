
from functools import wraps

def if_num(func):
    @wraps(func)
    def foo(*args,**kwargs):
        print(func.__name__)
        if isinstance(args[0],int):
            return func(*args,**kwargs)
        else:
            return func(0)
    return foo


@if_num
def one(num):
    return num**2

if __name__ == '__main__':
    one(6)
