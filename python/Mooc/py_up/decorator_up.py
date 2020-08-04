import time

def performance(f):
    ???

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)