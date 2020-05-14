import numpy as np

a = np.array([[1,2,3],[3,2,1]])
# print(a**2)
# print(a.sum())

# num = np.arange(100).reshape(10,10)
# print(num)
# 保存csv文件 二维数据
# np.savetxt('num.csv',num,fmt='%d',delimiter=',')

#读取csv文件
# n = np.loadtxt(fname='num.csv',dtype=np.float,delimiter=',')
# print(n)

#np数据存取
num = np.arange(100).reshape(2,10,5)
np.save('num.npy',num)
print(np.load('num.npy'))







