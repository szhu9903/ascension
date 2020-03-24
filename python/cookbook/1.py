'''
recode = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4)
]
def do_foo(x,y):
    print('foo',x,y)
def do_bar(s):
    print('bar',s)
for tag,*args in recode:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
'''

#队列
'''
from collections import deque
q = deque(maxlen = 5)
for i in range(11):
    if i>5:
        q.appendleft(i)
    else:
        q.append(i)
print(q)
'''

# deapq模块nlargest()最大的几个数、nsmallest()
'''
import heapq
num = [x for x in range(101) if x % 5==0]
print("nlardest找到最大的几个数：%s \n nlardest找到最小的几个数：%s"%(heapq.nlargest(3,num),heapq.nsmallest(3,num)))
'''


'''
# 字典计算
dic = {
    'zhu':100,
    'z':65.3,
    'h':45.2,
    's':98.6
}

print(min(dic,key = lambda k: dic[k]))
print(max(dic,key = lambda k: dic[k]))
'''

'''
#筛选序列中的元素
values = ['a','9','s','-','-6','6','2']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int,values))
print(ivals)
'''


result = {
    'join':45.3,
    'Tom':103,
    'M':195,
    'FB':10
}
#正常推倒式
p1 = {key:value for key,value in result.items() if value > 100}
#提高运行效率
p2 = dict((key,value) for key,value in result.items() if value > 100)

print(p2)

import os
a = os.urandom(20)
print(a)
b = a.decode('gbk')
print(b)







































                                          

















