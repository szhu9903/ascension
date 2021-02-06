
from flask import g
from comm import utilConfig
from comm import helper

class generalController(object):
    def __init__(self, module):
        # 数据库处理类
        self.module = module
        # 创建函数处理链路
        self.get_func_link = []
        self.post_func_link = []
        self.put_func_link = []
        self.delete_func_link = []
        # 初始化链路
        self.init_func_link()

    # 配置数据处理链
    def init_func_link(self):
        self.get_func_link.extend([self.before_deal_get_sys,
                                   self.service_deal_get_sys,
                                   self.after_deal_get_sys])
        self.post_func_link.extend([self.before_deal_post_sys,
                                    self.service_deal_post_sys,
                                    self.after_deal_post_sys])
        self.put_func_link.extend([self.before_deal_put_sys,
                                   self.service_deal_put_sys,
                                   self.after_deal_put_sys])
        self.delete_func_link.extend([self.before_deal_delete_sys,
                                      self.service_deal_delete_sys,
                                      self.after_deal_delete_sys])

    # 初始化请求数据
    def general_init_data(self, request):
        g.request = request
        g.para_data = request.args.to_dict()
        g.json_data = dict()

        g.exec_state = True
        g.info = 'OK'

        g.data = None

        if request.method in ['PUT', 'POST']:
            g.json_data.update(request.json)
        if request.method == 'GET':
            g.total_count = None
    # 统用处理流程执行链
    def execute_deal_service(self, check_link):
        for func in check_link:
            func()
            if not g.exec_state:
                break
    # 格式化返回数据
    def make_response_result(self):
        result = utilConfig.request_result
        result['req_info']['param'] = g.para_data
        result['ack_result']['status'] = 'OK' if g.exec_state else 'ERR'
        result['ack_result']['info'] = g.info
        if g.request.method == 'GET':
            result['ack_result']['count'] = g.total_count
            result['ack_result']['data'] = g.data
        if g.request.method in ['POST', 'PUT']:
            result['req_info']['data'] = g.json_data
        return result

    # 获取过滤条件语句
    def get_filter_sql(self):
        filter_str = g.para_data.get('filter')
        filter_sql = ''
        if filter_str:
            filter_list = filter_str.replace('|', ') and (')
            filter_sql = 'where (%s)' % filter_list.replace('$', ' or ')
            print(filter_str)
        return filter_sql
    # 获取排序语句
    def get_order_sql(self):
        order_str = g.para_data.get('order')
        order_sql = ''
        if order_str:
            order_sql = 'ORDER BY %s' % order_str.replace('|', ',')
        return order_sql
    # 获取分页数据
    def get_limit_sql(self):
        limit_str = g.para_data.get('limit')
        limit_sql = ''
        if limit_str:
            # 分页数，page:页码；pagesize:每页数据量
            page, page_size = limit_str.split(',')
            page_size = 1 if int(page_size) <= 1 else int(page_size)
            page = 0 if int(page) <= 1 else (int(page) - 1) * page_size
            limit_sql = 'limit %d, %d' % (page,page_size)
        return limit_sql

    # 获取记录数
    def get_data_count(self):
        # 获取过滤条件
        filter_sql = self.get_filter_sql()
        query_sql_count = '%s %s' % (self.module.sql_query_count,filter_sql)
        data = helper.get_db_data(query_sql_count)
        return data[0]['total_count'] if g.exec_state else None
    # 获取查询语句
    def get_query_default_sql(self):
        # TODO 默认查询，待完善条件、排序、分页等条件拼接
        default_query_sql = self.module.sql_query_default
        filter_sql = self.get_filter_sql()
        order_sql = self.get_order_sql()
        limit_sql = self.get_limit_sql()
        query_sql = '%s %s %s %s' % (default_query_sql, filter_sql, order_sql, limit_sql)
        return query_sql

    # 处理GET请求
    def deal_get_method(self, request):
        # 参数初始化处理
        self.general_init_data(request)
        # 执行处理流程
        self.execute_deal_service(self.get_func_link)
        return self.make_response_result()
    # GET 方法执行前处理
    def before_deal_get_sys(self):
        pass
    # GET 核心处理:获取数据
    def service_deal_get_sys(self):
        # 获取记录数
        total_count = self.get_data_count()
        if not g.exec_state:
            return
        g.total_count = total_count
        # 获取SQl语句
        query_sql = self.get_query_default_sql()
        # 获取数据集
        data = helper.get_db_data(query_sql)
        if not g.exec_state:
            return
        g.data = data

    # GET方法后处理
    def after_deal_get_sys(self):
        pass



    # 处理POST请求
    def deal_post_method(self, request):
        # 参数初始化处理
        self.general_init_data(request)
        # 统用处理链
        self.execute_deal_service(self.post_func_link)
        return self.make_response_result()
    # 前置
    def before_deal_post_sys(self):
        pass
    # 处理POST业务
    def service_deal_post_sys(self):
        # 获取插入语句
        # TODO 检查请求数据格式，在此处或 request_before, 检查提交数据名称
        insert_data = g.json_data
        # 获取SQL语句
        insert_sql = self.module.sql_insert_form_data(insert_data['req_info']['data'])
        row = helper.execute_db_sql(insert_sql, insert_data['req_info']['data'])
        if not g.exec_state:
            return
        g.row = row
    # 后置
    def after_deal_post_sys(self):
        pass



    # 处理PUT请求
    def deal_put_method(self, request):
        # 参数初始化处理
        self.general_init_data(request)
        # 处理链
        self.execute_deal_service(self.put_func_link)
        return self.make_response_result()
    # 前置处理
    def before_deal_put_sys(self):
        pass
    # PUT 业务处理
    def service_deal_put_sys(self):
        recid = g.request.view_args.get('record_id')
        update_data = g.json_data
        print(update_data)
        # 获取SQL 语句
        update_sql = self.module.sql_update_from_data(update_data['req_info']['data'], recid)
        row = helper.execute_db_sql(update_sql, update_data['req_info']['data'])
        if not g.exec_state:
            return
        g.row = row
    # 后置处理
    def after_deal_put_sys(self):
        pass



    # 处理DELETE请求
    def deal_delete_method(self, request):
        # 参数初始化处理
        self.general_init_data(request)
        # DELETE 处理链
        self.execute_deal_service(self.delete_func_link)
        return self.make_response_result()
    # 前置处理
    def before_deal_delete_sys(self):
        pass
    # DELETE 业务处理
    def service_deal_delete_sys(self):
        recid = g.request.view_args.get('record_id')
        # 获取删除语句
        sql_delete = self.module.sql_delete_form_data(recid)
        row = helper.execute_db_sql(sql_delete)
        if not g.exec_state:
            return
        g.row = row

    # 后置处理
    def after_deal_delete_sys(self):
        pass
