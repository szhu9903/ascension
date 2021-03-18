
# 有序插入元素 保持顺序
from bisect import insort
import random
def insert_sort():
    my_list = []
    for i in range(7):
        new_item = random.randrange(14)
        insort(my_list,new_item)
        print('%2d ->'%new_item,my_list)
    return my_list

print(insert_sort())

a = ['a','b','c']
b = [1,2,30]
c = [dict(zip(a,b))]
print(c)
