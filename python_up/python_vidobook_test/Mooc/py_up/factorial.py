
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

from functools import reduce
def factorial2(n):
    return reduce(lambda x,y:x*y,range(1,n+1))


if __name__=='__main__':
    print(factorial(5))
    print(factorial2(5))
