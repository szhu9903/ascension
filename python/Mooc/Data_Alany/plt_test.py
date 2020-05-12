# -*- coding: 'utf-8' -*-
import matplotlib.pyplot as plt

#创建数据图形
data = [9,6,3,2,5,8,7,4,1,2,3,6,5,4,7,8,9,5,1,4,7,5,3,6,9]
plt.plot(data)
#xy轴name
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.axis([0, len(data)+1, 0, 10])
plt.show()





