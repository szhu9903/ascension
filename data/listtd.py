#列表推导和生成器表达式
'''
a = [i for i in range(0,101,5) if i>50]

colors = ['black','white']
sizes = ['S','M','L']
b = [(color,size) for color in colors for size in sizes]
'''


#具名元组
'''
from collections import namedtuple
User = namedtuple('User','name age phone')#类名，参数
tokyo = User('朱帅杰','22',(159,9409,2160))
print(User._fields)
'''

#列表排序
'''
fruits=['app','brind','success','error','zonononoon']
print(sorted(fruits,key=len,reverse=False))
print(fruits)
'''



'''
from array import array
from random import random
floats = array('d',(random() for i in range(10**7)))
print(floats[-1])
with open('floats.bin','wb') as f:
	floats.tofile(f)#将数据添加到floats.bin里
floats2 = array('d')#新建双浮点空数组
with open('floats.bin','rb') as g:
	floats2.fromfile(g,10**7)
print(floats2[-1])
if floats2 == floats:
	print('YES')
'''



#NumPy和SciPy提供高阶数组和矩阵操作
'''
import numpy
a = numpy.arange(12)
print(a.shape)#查看数组的维度
a.shape = 3,4#把数组转换成二维数组
print(a.transpose())#二维数组行列交换
'''

#52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
'''
list = [2,3,5,4,9,6]
new_list = []
def get_min(list):
	a = min(list)
	list.remove(a)
	new_list.append(a)
	if len(list)>0:
		get_min(list)
	return new_list

new_list = get_min(list)
print(new_list)
'''

#写一个单列模式

class Singleton(object):
	__instance = None
	def __new__(cls,name,age):
		if not cls.__instance:
			print('aaaaaaaaaaaaa')
			cls.__instance = object.__new__(cls)
		print('bbbbbbbbbbbbbbb')
		return cls.__instance

a = Singleton('朱帅杰',22)
print('ccccccccccccccccccccc')
b = Singleton('张',21)
print(id(a))
print(id(b))

b.age = 99
print(a.age)













