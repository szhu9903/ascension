import logging
import flask_login
from . import user
from comm import utilConfig
from comm.userBase import userBase
from flask import jsonify
from flask import request
from resource import login_message

logger = logging.getLogger('app')

@user.route('/login/', methods = ['POST'])
def login():
    result = utilConfig.request_result
    try:
        user_info = request.json
        if not user_info.get('req_info'):
            result['ack_result']['status'] = 'ERR_PARA'
            result['ack_result']['info'] = '错误请求消息！'
            logger.info('res data:(result=%s, info=%s)' % (result['ack_result']['status'],
                                                        result['ack_result']['info']))
            return jsonify(result)
        if not user_info['req_info'].get('data'):
            result['ack_result']['status'] = 'ERR_PARA'
            result['ack_result']['info'] = '错误请求消息'
            logger.info('res data:(result=%s, info=%s)' % (result['ack_result']['status'],
                                                           result['ack_result']['info']))
            return jsonify(result)
        result['req_info']['data'] = user_info['req_info']['data']
        user_name = user_info['req_info']['data'].get('user_name')
        user_pwd = user_info['req_info']['data'].get('user_pwd')
        if not (user_name and user_pwd):
            result['ack_result']['status'] = 'ERR_PARA'
            result['ack_result']['info'] = '错误:缺少用户名或密码'
            logger.info('res data:(result=%s, info=%s)' % (result['ack_result']['status'],
                                                           result['ack_result']['info']))
            return jsonify(result)
        user_id = userBase.user_id(user_name)
        if not user_id:
            result['ack_result']['status'] = 'ERR_PARA'
            result['ack_result']['info'] = '用户不存在'
            logger.info('res data:(result=%s, info=%s)' % (result['ack_result']['status'],
                                                           result['ack_result']['info']))
            return jsonify(result)
        user = userBase(user_id)
        if not user.check_pwd(user_pwd):
            result['ack_result']['status'] = 'ERR_PARA'
            result['ack_result']['info'] = '密码校验失败'
            logger.info('res data:(result=%s, info=%s)' % (result['ack_result']['status'],
                                                           result['ack_result']['info']))
            return jsonify(result)
        flask_login.login_user(user)
    except Exception as Err:
        result['ack_result']['status'] = 'ERR'
        result['ack_result']['info'] = '测试过程!'
        result['ack_result']['data'] = '测试过程!'
    return jsonify(result)


@login_message.user_loader
def load_user(user_id):
    return userBase.get(user_id)



