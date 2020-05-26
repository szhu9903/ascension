import pandas as pd
import numpy as np

#pandas数据类型Series
# num = pd.Series([5,6,2,1],index=['a','s','d','f'])
# print(num.get('a'))

# pandas数据类型DataFrame
data = {'城市':['河南','浙江'],
        '人口':[22,23]}
# num = pd.DataFrame(np.arange(10,30).reshape(4,5))
num = pd.DataFrame(data=data,index=['a','b'])
#reindex 重新索引
num1 = num.reindex(index=['b','a','c'],columns=['人口','城市'],fill_value=0)
print(num1.sort_index(axis=1,ascending=True))