
from comm import tableModule

from datetime import timedelta


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

