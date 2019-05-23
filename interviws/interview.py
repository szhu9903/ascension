#22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
'''
s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort(reverse=False)
res = ''.join(s)
print(s)
'''

#23、用lambda函数实现两个数相乘
'''
sum = lambda a,b:a*b
print(sum(4,5))
'''

#24、字典根据键从小到大排序
'''
dic = {"name":"zs","age":18,"city":"许昌","tel":"1362626627"}
lis = sorted(dic.items(),key=lambda i:i[0],reverse=False)
print(dict(lis))
'''

#26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"
'''
import re
a = "not 404 found 张三 99 深圳"
list = a.split(' ')
#p匹配非重复的正则，返回一个列表，然后删除两个列表重复的部分
res = re.findall('\d+|[a-zA-Z]+',a)
for i in res:
	if i in list:
		list.remove(i)
new_list = ' '.join(list)
print(new_list)
'''

#27、filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],列表推倒式
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fn(a):
	return a%2 == 1
g = filter(fn,a)
print(g)
new_list = [i for i in g]
print(new_list)

new_lists = [i for i in a if i%2 == 1]
print(new_lists)
'''

#打印现在的时间
'''
import datetime
a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) +'星期'+ str(datetime.datetime.now().isoweekday())
print(a)
'''

#39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
'''
a = [[1,2],[3,4],[5,6]]
new_list = [i for j in a for i in j]
print(new_list)
'''

#71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
'''
list = [0,-1,3,-10,5,9]
print(id(list))
list.sort(reverse = False)
print(id(list),list)
print('----------sort在列表的基础上做出排序，sorted生成一个新的列表----------')

list = [0,-1,3,-10,5,9]
print(id(list))
# res = sorted(list,reverse=False)
res = sorted(list,key = lambda x:(x<0,abs(x)))#abs()绝对值
print(id(res),res)
'''
#74、列表嵌套字典的排序，分别根据年龄和姓名排序
'''
foo = [{"name":"zs","age":19},{"name":"ll","age":54},
{"name":"wa","age":17},{"name":"df","age":23}]

a = sorted(foo,key = lambda x:x['age'])
print(a)
a = sorted(foo,key = lambda x:x['name'])
print(a)
'''
# 78、根据键对字典排序（方法二,不用zip)
# dic = {'name','red','man','good','nice'}
# a = sorted(dic.items(),key=lambda x:x[0])
# new_dic = {i[0]:i[1] for i in a}


#生成器
'''
import random

dic = {k:random.randint(5,10) for k in ['a','b','c','d']}
print(dic)
'''

#递归求和
'''
def get_num(num):
	if num>0:
		res = num+get_num(num-1)
	else:
		res = 0
	return res
print(get_num(100))
'''

#101、求两个列表的交集、差集、并集

'''
a = [1,2,3,4]
b = [3,4,5,6]

print('交集：',[i for i in a if i in b])
print('交集:',list(set(a).intersection(set(b))))

print('并集:',list(set(a).union(set(b))))

print('差集：',list(set(a).difference(set(b))))
print('差集：',list(set(b).difference(set(a))))
'''


#迭代器，适合遍历比较巨大的集合。__iter__:返回迭代器本身，__next__：返回容器中下一个元素或数据
'''
for x in range(101):
	print('生成%s'%x)
'''

#生成器，带有yield的函数，当函数被调用时返回一个生成器对象，生成器函数生成值后会自动挂起并暂停他们的执行状态
'''
def myyield(n):
	while n>=0:
		print('生成%s'%n)
		yield n
		n -= 1
print([n for n in myyield(100)])
'''







# import copy

# # a = [x for x in range(11)]
# # b = copy.deepcopy(a)
# # c = copy.copy(a)
# # c.insert(0,'Hello')
# # print('a:%s\nb:%s\nc:%s'%(a,b,c))

# roots = {'%s的平方'%x:x**2 for x in range(11)}
# print(roots)


# with open('max.txt') as max:
# 	count = 0
# 	for i in max.read():
# 		if i.islower():
# 			count += 1
# print(count)


# from random import shuffle

# a = [x for x in range(11)]
# shuffle(a)
# print(a)

#进制转换
'''
print(bin(8))
print(oct(8))
print(hex(8))

a = {'%s is square'%i:i**2 for i in range(11)}
b = a.keys()
print(a)
print(b)
'''


# fcount = '3'
# money = '50'
# fmoney = int(fcount)*int(money)
# print(type(fmoney))
# print(fmoney)


import datetime

time = datetime.datetime.now()
print(time)























