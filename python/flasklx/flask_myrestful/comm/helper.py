import json
import logging
from decimal import Decimal
from comm import db
from flask import g

logger = logging.getLogger('app')

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        super(JSONEncoder, self).default(o)


# 执行SQl,获取结果集
def get_db_data(query_sql):
    res_data = None
    db_connection = db.get_normal_connect
    cursor = db_connection.cursor()
    try:
        cursor.execute(query_sql)
        res_data = cursor.fetchall()
    except Exception as err:
        logger.exception('数据库执行失败(%s)' % query_sql)
        g.exec_state = False
        g.info = '错误,数据库执行失败(%s).' % str(err)
    cursor.close()
    db.resume_normal_connect(db_connection)
    return res_data

# 执行SQl
def execute_db_sql(execute_sql, param_data=None):
    rec_id = None
    insert_sql = execute_sql
    if param_data:
        insert_sql = execute_sql % param_data
    db_connection = db.get_normal_connect()
    cursor = db_connection.cursor()
    try:
        cursor.execute(insert_sql)
        rec_id = cursor.lastrowid
    except Exception as err:
        logger.exception('数据库执行失败(%s)' % insert_sql)
        g.exec_state = False
        g.info = '错误,数据库执行失败(%s).' % str(err)
    cursor.close()
    db.resume_normal_connect(db_connection)
    return rec_id



