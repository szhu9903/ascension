import numpy as np

'''
#测试数据
my_array = np.array([1,2,3,4,5])

#查看创建数组的形状
print(my_array.shape)

#创建数组
my_new_array = np.zeros((5))
my_new_array1 = np.random.random((5))
#创建二维数组
my_new_tow_array = np.ones((5,3))
print(my_new_tow_array)

#numpy数组操作
a = np.array([[2.6,9.0],[4.6,5.8]])
b = np.array([[1.4,5.9],[8.2,6.3]])
sum = a+b
difference = a-b
product = a*b
quotient = a/b
#print('sum = %s \n difference = %s \n product = %s \n quotient = %s'%(sum,difference,product,quotient))

#二维数组切片
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])
print(a[3,4])
print(a[::2,::2])

# 根据列表中间的数字进行分割列表，循环查询
def quick(arr):
	if len(arr) <=1:
		return arr
	privot = arr[len(arr)//2]
	left = [x for x in arr if x<privot]
	middle = [x for x in arr if x==privot]
	reght = [x for x in arr if x>privot]
	return quick(left) + middle + quick(reght)
print(quick([1,5,6,7,9,165,6,454,5,14]))


#矩阵运算（add,subtract,multiply,divide）
x = np.array([[1,2],[3,4]],dtype = np.float64)
y = np.array([[5,6],[7,8]],dtype = np.float64)
# print(np.add(x,y))#加
# print(np.subtract(x,y))#减

#要转置一个矩阵，只需使用一个数组对象的T属性
print(x.T)
'''


# 快速统计
'''
import pandas as pd
import numpy as np
dates = pd.date_range('20190101',periods=7)
df = pd.DataFrame(np.random.randn(7,4),index=dates,columns=list('ABCD'))
# 快速统计
print(df.describe())
'''


# pandas 系列(Series)
'''
import pandas as pd
import numpy as np

# 创建空系列
s = pd.Series()

# 从ndarray创建一个系列
data = np.array(['A','B','C','D','E'])
s = pd.Series(data,index=[100,99,98,97,96])

# 从字典创建一个系列
data = {'A':1.,'B':2.,'C':3.}
s = pd.Series(data,index=['A','D','B','C'])

# 从具体位置的系列访问数据
s = pd.Series([1,2,3,4,5,6],index = ['A','B','C','D','E','F'])
print(s[3:])
'''


# pandas 数据帧(DataFrame),二维数组
'''
import pandas as pd

# 创建空的DataFrame
df = pd.DataFrame()

# 从列表创建DataFrame
data = [['z',12],['h',30],['u',22]]
df = pd.DataFrame(data,columns = ['name','age'],dtype = float)

# 从ndarrays/Lists的字典来创建DataFrame
data = {"Name":['zhu','re','huang','yao','zhang'],'age':[22,23,21,25,26]}
df = pd.DataFrame(data)

# 列添加
d = {'one':pd.Series([1,2,3],index = ['A','B','C']),'tow':pd.Series([1,2,3,4],index = ['A','B','C','D'])}
df = pd.DataFrame(d)
df['three'] = pd.Series([10,20,30],index = ['A','B','C'])
df['four'] = df['one'] + df['three']
print(df)
'''


# pandas 面板(Panel),三维数组
'''
import numpy as np
import pandas as pd

# 从3D ndarray创建
data = np.random.rand(2,4,5)
p = pd.Panel(data)

# 从DataFrame的dict对象创建面板
data = {'Item1':pd.DataFrame(np.random.randn(4,3)),
        'Item2':pd.DataFrame(np.random.randn(4,2))}
p = pd.Panel(data)
'''

# pandas 基础功能
'''
import pandas as pd
import numpy as np

data = {
    'Name': pd.Series(['zhu','shuai','jie','rere','wei','da','zhang','huang']),
    'Age' : pd.Series([22,32,15,15,64,64,64,62]),
    'Rating': pd.Series(['A','B','A','C','A','A','C','B'])
        }
print(pd.DataFrame(data).T)
'''
re = []
a = {'felec_before': 2718.0, 'felec_after': 2802.0, 'index': 6.0, 'fcost_room_num': 4106.0, 'fstart_date': '2019-06-25', 'felec_all': 84.0, 'fend_date': '2019-07-25', 'fremark': 'nan'}
for key in a:
	if type(a[key]) is float:
		a[key] = int(a[key])
re.append(a)
print(re)











































