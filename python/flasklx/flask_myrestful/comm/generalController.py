
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

        # 初始化链路
        self.init_func_link()

    def init_func_link(self):
        self.get_func_link.extend([self.before_deal_get_sys,
                                   self.service_deal_get_sys,
                                   self.after_deal_get_sys])


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

    # GET 方法执行前处理
    def before_deal_get_sys(self):
        pass

    # 获取过滤条件语句
    def get_filter_sql(self):
        filter_str = g.para_data.get('filter')
        filter_sql = ''
        if filter_str:
            # TODO 过滤条件待完善
            pass
        return filter_sql

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
        query_sql = self.module.sql_query_default
        return query_sql
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

    # 处理GET请求
    def deal_get_method(self, request):
        # 参数初始化处理
        self.general_init_data(request)
        # 执行处理流程
        self.execute_deal_service(self.get_func_link)
        return self.make_response_result()

    # 处理POST请求
    def deal_post_method(self, request):
        # 参数初始化处理
        self.general_init_data(request)

    # 处理PUT请求
    def deal_put_method(self, request):
        # 参数初始化处理
        self.general_init_data(request)

    # 处理DELETE请求
    def deal_delete_method(self, request):
        # 参数初始化处理
        self.general_init_data(request)