"""
python 高阶函数 ：接收函数为参数函数 map
"""

def format_name(name):
    return name[0].upper() + name[1:].lower()

from functools import reduce
# reduce 接收两个参数，将第一轮结果继续
def prod(num_a,num_b):
    return num_a*num_b

#1-100 平方根为整数
import math
def is_sqr(num):
    r = int(math.sqrt(num))
    return r*r==num




if __name__ == '__main__':

    # function list
    # new_name = map(format_name,['admin','LISA','brRt'])
    # print(list(new_name))

    # new_num = reduce(prod,[2,4,5,7,12])
    # print(new_num)
    new_sqr = filter(is_sqr,range(1,100))
    print(list(new_sqr))



