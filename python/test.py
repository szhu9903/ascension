# import requests, json
#
# class RequestTest(object):
#     def __init__(self, module_name):
#         self.url = "http://127.0.0.1:8005/api/v1.0/config/%s/"%module_name
#         self.headers = {'user-agent':'Mozilla/5.0','Content-Type':'application/json'}
#         self.cookies = self.login_response_data().cookies
#
#     def get_response_data(self):
#         response_data = requests.get(self.url,
#                                      timeout = 30,
#                                      headers = self.headers,
#                                      cookies=self.cookies)
#         response_data.raise_for_status()
#         response_data.encoding = 'utf-8'
#         res = response_data.json()
#         return res
#
#     def delete_response_data(self, del_id):
#         del_url = self.url + str(del_id) + '/'
#         response_data = requests.delete(url = del_url,
#                                         timeout = 30,
#                                         headers = self.headers,
#                                         cookies=self.cookies)
#         response_data.raise_for_status()
#         response_data.encoding = 'utf-8'
#         res = response_data.json()
#         return res['ack_result']['status']
#
#     def login_response_data(self):
#         url = "http://127.0.0.1:8005/api/v1.0/commfunc/login/"
#         post_data = {
#             "req_info":{
#                 "data":{
#                     "user_name": "hudeli",
#                     "user_password": "12345 ",
#                     "terminal_type": "APP",
#                     "adid":1
#                 }
#             }
#         }
#         response_data = requests.post(url,
#                                       data = json.dumps(post_data),
#                                       headers = self.headers)
#         response_data.raise_for_status()
#         response_data.encoding = 'utf-8'
#         return response_data
#
#
#
# if __name__ == '__main__':
#     ratio = RequestTest('ConfigRatio')
#     data = ratio.get_response_data()
#     result = None
#     if data['ack_result']['data']:
#         id_list = [data['id'] for data in data['ack_result']['data']]
#         result = list(map(ratio.delete_response_data,id_list))
#     print(result)

"""
DBUtils python管理数据库的包，可自动管理连接对象的创建与释放，常用外部接口
PersistentDB:提供线程专用数据库连接，并自动管理连接
PooledDB:提供线程间可共享的数据库连接，并能自动管理连接
"""

import pymysql
from DBUtils.pooled_db import PooledDB,SharedDBConnection
# 创建线程池,配置项，源码说明
pool = PooledDB(pymysql, 5, host="127.0.0.1", user='root',
                passwd='1017', db='erpdb_test', port=3306, charset="utf8")
# 从线程池获取连接
conn = pool.connection()
# 创建游标
cur = conn.cursor()
r = cur.execute("select * from user_base").fetchall()
print(r)
cur.close()
conn.close()























