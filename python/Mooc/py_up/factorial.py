
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)



if __name__=='__main__':
    print(factorial(5))

