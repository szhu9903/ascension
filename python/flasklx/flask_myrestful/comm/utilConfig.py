import logging

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
    'ack_info': {
        'status': 'OK',
        'info': 'OK',
        'data': None
    }
}

