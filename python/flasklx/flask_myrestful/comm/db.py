
from resource import *
import pymysql
import logging

# 获取日志输出句柄
logger = logging.getLogger('app')


# 创建列表作为数据库连接池使用
connection_normal_pool = []

# 服务启动，初始化创建二十个固定数据库连接到数据库链接池
def register_db_helper(db_conf):
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


# 执行SQl,获取结果集
def get_db_data(query_sql):
    res_data = None
    db_connection = get_normal_connect()
    cursor = db_connection.cursor()
    try:
        cursor.execute(query_sql)
        res_data = cursor.fetchall()
    except Exception as err:
        logger.exception('数据库执行失败(%s)' % query_sql)
        g.exec_state = False
        g.info = '错误,数据库执行失败(%s).' % str(err)
    cursor.close()
    resume_normal_connect(db_connection)
    return res_data

# 执行SQl
def execute_db_sql(execute_sql, param_data=None):
    rec_id = None
    insert_sql = execute_sql
    if param_data:
        insert_sql = execute_sql % param_data
    db_connection = get_normal_connect()
    cursor = db_connection.cursor()
    try:
        cursor.execute(insert_sql)
        rec_id = cursor.lastrowid
    except Exception as err:
        logger.exception('数据库执行失败(%s)' % insert_sql)
        g.exec_state = False
        g.info = '错误,数据库执行失败(%s).' % str(err)
    cursor.close()
    resume_normal_connect(db_connection)
    return rec_id