import numpy as np


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


