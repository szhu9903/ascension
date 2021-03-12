
"""
DBUtils python管理数据库的包，可自动管理连接对象的创建与释放，常用外部接口
PersistentDB:提供线程专用数据库连接，并自动管理连接
PooledDB:提供线程间可共享的数据库连接，并能自动管理连接
"""

import pymysql
import threading
import time
from DBUtils.PooledDB import PooledDB
# 创建线程池,配置项，源码说明
pool = PooledDB(creator = pymysql, # 使用的连接模块
                maxconnections = 20, # 连接池允许的最大连接数，0和None表示无限制
                mincached = 10, # 初始化时，连接池至少要创建的空闲连接，0表示不创建
                maxcached = 20, # 链接池最大空闲链接数量
                blocking = True, # 是否阻塞等待
                maxshared = 5, # 连接池最大可共享连接数量，无效
                maxusage = None, # 一个链接最多被复用次数，None表示无限复用
                host = "127.0.0.1",
                port = 3306,
                user = 'root',
                passwd = '1017',
                db = 'erpdb_test',
                charset = "utf8")

def func(i):
    # 从数据库连接池获取连接,shareable:是否共享链接
    conn = pool.connection(shareable = False)
    print("start %s" % i)
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from user_base")
    res = cursor.fetchall()
    print("finish data %s %s" % (i, res))
    conn.close()


for i in range(10):
    th = threading.Thread(target = func, args = (i, ))
    th.start()
















