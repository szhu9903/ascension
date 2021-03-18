
import logging
from comm import db

logger = logging.getLogger('app')

class tableModule(object):
    def __init__(self, tablename):
        self.tablename = tablename
        self.init_table_mate()

    # 初始化表属性
    def init_table_mate(self):
        # 初始化列信息
        self.colnames, self.coltypes = self.get_col_info()
        self.meta = dict(zip(self.colnames, self.coltypes))
        # 构建SQL语句段
        colkey_str = ','.join(self.colnames) # col1,col2,col3
        colval_str = '"%(' + ')s","%('.join(self.colnames) + ')s"'  # "%(col1)s","%(col2)s","%(col3)s"
        self.sql_query_default = 'select %s from %s' % (colkey_str, self.tablename)
        self.sql_insert_default = 'insert into %s(%s) values(%s)' % (self.tablename, colkey_str, colval_str)
        self.sql_delete_default = 'delete from %s ' % self.tablename
        self.sql_query_count = 'select count(*) as total_count from %s ' % self.tablename


    # 表结构属性
    def get_col_info(self):
        db_connection = db.get_normal_connect()
        cursor = db_connection.cursor()
        colname_list = []
        coltype_list = []
        try:
            cursor.execute('select * from %s where zid=0' % self.tablename)
        except Exception as err:
            logger.exception('error to init %s:%s' % (self.tablename, str(err)))
        else:
            fields =cursor.description
            for field in fields:
                colname_list.append(field[0])
                coltype_list.append(field[1])
        cursor.close()
        db.resume_normal_connect(db_connection)
        return colname_list, coltype_list

    # 获取insert语句
    def sql_insert_form_data(self, data):
        data_unit = data
        new_col_list = data_unit.keys()
        # new_col_list = [col for col in self.colnames if col in data_unit.keys()]
        colnamestr = '`' + '`,`'.join(new_col_list) + '`'
        colvalstr = '"%(' + ')s","%('.join(new_col_list) + ')s"'
        sql_insert = "insert into %s (%s) values(%s)" % (self.tablename, colnamestr, colvalstr)
        return sql_insert

    # 获取update语句
    def sql_update_from_data(self, data, recid):
        print(data)
        col_list = data.keys()
        new_col_list = []
        for col_name in col_list:
            new_col_list.append('%s="%%(%s)s"' % (col_name, col_name))
        sql_update = "update %s set %s WHERE zid=%s " % (self.tablename, ','.join(new_col_list), recid)
        return sql_update

    # 获取delete语句
    def sql_delete_form_data(self, recid):
        sql_delete = '%s where zid=%s' % (self.sql_delete_default, recid)
        return sql_delete

