# import matplotlib.pyplot as plt

# plt.plot([0,2,6,7,8,9],[1,2,3,4,5,6])
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.axis([-1,10,0,7])
# plt.show()

# import matplotlib.pyplot  as  plt
# import numpy as np
# from random import choice
# import matplotlib
#
# #全局设置字体
# # matplotlib.rcParams['font.family'] = 'SimHei'
# # matplotlib.rcParams['font.size'] = 16
#
# num_all = []
# index = 1.5
# rgb = ['b--','g-.','r:','c:','m:']
# for i in range(5):
#     a = np.arange(10)
#     plt.plot(a,a*index,choice(rgb))
#     index += 1
#
# #局部设置字体
# plt.xlabel('X轴',fontproperties='SimHei',fontsize=16)
# plt.ylabel('Y轴',fontproperties='Kaiti',fontsize=16)
# plt.show()



# 正弦波cos
# import matplotlib.pyplot as plt
# import numpy as np
#
# num = np.arange(-2*np.pi,2*np.pi,0.02)
# plt.plot(num,np.sin(num),'r--')
#
# plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=16)
# plt.ylabel('纵轴：振幅',fontproperties='SimHei',fontsize=16)
# plt.title(r'正弦$y=sin(\pi x)$',fontproperties='SimHei',fontsize=25)
#
# plt.axis([-3*np.pi,3*np.pi,-2,2])
# plt.grid(True)
# plt.show()


# plt基础函数，绘制饼形图
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 16

labels = '一月份','二月份','三月份','四月份','五月份','六月份'
sizes = [10,20,30,5,10,25]
explode = (0,0,0,0,0.1,0)


plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=False,startangle=90)
plt.axis('equal')
plt.show()










