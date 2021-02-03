import logging
from comm import tableModule

# 初始化日志
applog = logging.getLogger('app')
applog.setLevel(logging.DEBUG)

appHandle = logging.StreamHandler()
appFormatter = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")
appHandle.setLevel(logging.DEBUG)
appHandle.setFormatter(appFormatter)

applog.addHandler(appHandle)


# 初始化JSON标准结构

request_result = {
    'req_info': {
        'param': None,
        'extparam': None,
        'data': None
    },
    'ack_result': {
        'status': 'OK',
        'info': 'OK',
        'data': None
    }
}


table_config = {
    'zsjblog': tableModule.tableModule('zsj_blog'),
    'zsjblogtype': tableModule.tableModule('zsj_blog_type'),
    'zsjbloguser': tableModule.tableModule('zsj_blog_user')
}

