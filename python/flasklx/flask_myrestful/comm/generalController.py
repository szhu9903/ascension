
from flask import g
from comm import utilConfig

class generalController(object):
    def __init__(self):
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

        if request.methods in ['PUT', 'POST']:
            g.json_data.update(request.json)
        if request.methods == 'GET':
            g.count = None

    # 统用处理流程执行链
    def execute_deal_service(self, check_link):
        for func in check_link:
            func()
            if not g.exec_state:
                break

    # GET 方法执行前处理
    def before_deal_get_sys(self):
        pass

    def get_data_count(self):
        pass
    def get_query_default_sql(self):
        pass

    # GET 核心处理:获取数据
    def service_deal_get_sys(self):
        # 获取记录数
        total_count = self.get_data_count()
        # 获取SQl语句
        query_sql = self.get_query_default_sql()


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
            result['ack_result']['count'] = g.count
            result['ack_result']['data'] = g.data
        if g.request.method in ['POST', 'PUT']:
            result['req_info']['data'] = g.json_data
        return result

    # 处理GET请求
    def deal_get_method(self, request):
        # 参数初始化处理
        self.general_init_data(request)
        # 执行处理流程

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