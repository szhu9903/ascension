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


# pandas DataFrame对指定列数据进行汇总，生成汇总行
# 读取json数据，cls=JSONEncode,我的数据存在decimal类型数据转换
pd_data = pd.read_json(json.dumps(data, cls=JSONEncoder), orient='records')
# 汇总所有为小计的行，生成汇总行数据，要对小计行中的部分指定的列进行汇总
pd_data.loc[0] = pd_data[pd_data['id'] == '小计'].apply(filter_dataframe)
# 转换回json
p = json.loads(pd_data.to_json(orient='records'))

# 自定义处理函数
def filter_dataframe(col):
    # col.name 对应读取每一列的标题，可在DEBUG中找到
    if col.name == 'id':
        col = '合计'
    elif col.name in ['sc_vtotalcapacity', 'sc_vfinishtotalcapacity', 'sc_confirmpaid',
                  'oil_cost', 'tong_mon', 'bill_count', 'send_count', 'order_count', 'add_distance']:
        col = col.sum()
    else:
        col = ''
    return col
