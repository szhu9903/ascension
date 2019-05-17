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


ffood_list = [{"name":"豪华","number":"1","id":"1"},{"name":"豪华","number":"1","id":"2"}]

for i in range(len(ffood_list)):
    for value in i.itervalues():
        print('value')
