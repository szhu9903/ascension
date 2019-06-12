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

'''
#队列
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








































                                          

















