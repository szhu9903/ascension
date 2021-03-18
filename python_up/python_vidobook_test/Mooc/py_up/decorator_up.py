import time
from functools import reduce
import datetime

def performance(f):
    def fun(*args,**kwargs):
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(date)
        start_date = time.time()
        res = f(*args,**kwargs)
        end_date = time.time()
        print(end_date-start_date)
        return res
    return fun

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(10))