
from resource import *
import pymysql
import logging

# 获取日志输出句柄
logger = logging.getLogger('app')


# 创建列表作为数据库连接池使用
connection_normal_pool = []

# 服务启动，初始化创建二十个固定数据库连接到数据库链接池
def db_init():
    global connection_normal_pool
    for i in range(20):
        # 创建数据库连接
        connection = pymysql.Connect(host = db_conf['host'],
                                     port = db_conf['port'],
                                     user = db_conf['user'],
                                     password = db_conf['password'],
                                     db = db_conf['db_name'],
                                     charset = db_conf['charset'],
                                     cursorclass = pymysql.cursors.DictCursor)
        # 是否开启数据库提交事务
        connection.autocommit(True)
        connection_normal_pool.append(connection)


# 从连接池获取空闲数据库连接
def get_normal_connect():
    db_connection = None
    try:
        db_connection = connection_normal_pool.pop()
        db_connection.ping(reconnect = True)
    except Exception as Err:
        logger.info('normal_pool_error %s' % Err)
    return db_connection

# 将使用后的连接放回数据库连接池中
def resume_normal_connect(connection):
    try:
        connection_normal_pool.insert(0, connection)
    except Exception as Err:
        logger.info('resume connection Error %s' % Err)

db_init()