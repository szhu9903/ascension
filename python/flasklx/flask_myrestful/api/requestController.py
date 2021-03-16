
import logging
import json
from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Blueprint
from comm import utilConfig
from flask_login import login_required
from flask_login import current_user
from comm.generalController import generalController

main = Blueprint('main', __name__)

logger = logging.getLogger('app')

genral_config = {
    'zsjblog' : generalController(utilConfig.table_config['zsjblog']),
    'zsjblogtype' : generalController(utilConfig.table_config['zsjblogtype']),
    'zsjbloguser' : generalController(utilConfig.table_config['zsjbloguser'])
}

# 统一GET处理
@main.route('/<string:config_name>/', methods=['GET'])
@login_required
def genral_get(config_name):
    try:
        logger.info('request [GET:%s]-->%s', request.path, request.args.to_dict())
        if config_name.lower() in genral_config.keys():
            result = genral_config[config_name.lower()].deal_get_method(request)
        else:
            result = utilConfig.request_result
            result['ack_result']['status'] = 'ERR'
            result['ack_result']['info'] = '未匹配到视图! [%s]' % config_name
    except Exception as err:
        result = utilConfig.request_result
        result['ack_result']['status'] = 'ERR'
        result['ack_result']['info'] = '未匹配到视图! [%s]' % str(err)
    logger.info('res data[%s]:(result=%s, info=%s)' % (request.path, result['ack_result']['status'], result['ack_result']['info']))
    return jsonify(result)

# 统一POST处理
@main.route('/<string:config_name>/', methods=['POST'])
def genral_post(config_name):
    try:
        logger.info('request [POST:%s][para:%s]-->%s', request.path, request.args.to_dict(), request.json)
        if config_name.lower() in genral_config.keys():
            result = genral_config[config_name.lower()].deal_post_method(request)
        else:
            result = json.loads(utilConfig.request_result)
            result['ack_result']['status'] = 'ERR'
            result['ack_result']['info'] = '未匹配到视图! [%s]' % config_name
    except Exception as err:
        result = json.loads(utilConfig.request_result)
        result['ack_result']['status'] = 'ERR'
        result['ack_result']['info'] = '未匹配到视图! [%s]' % str(err)
    logger.info('res data[%s]:(result=%s, info=%s)' % (request.path, result['ack_result']['status'], result['ack_result']['info']))
    return jsonify(result)

# 统一PUT处理
@main.route('/<string:config_name>/<int:record_id>/', methods=['PUT'])
def genral_put(config_name, record_id):
    try:
        logger.info('request [POST:%s][para:%s]-->%s', request.path, request.args.to_dict(), request.json)
        if config_name.lower() in genral_config.keys():
            result = genral_config[config_name.lower()].deal_put_method(request)
        else:
            result = json.loads(utilConfig.request_result)
            result['ack_result']['status'] = 'ERR'
            result['ack_result']['info'] = '未匹配到视图! [%s]' % config_name
    except Exception as err:
        result = json.loads(utilConfig.request_result)
        result['ack_result']['status'] = 'ERR'
        result['ack_result']['info'] = '未匹配到视图! [%s]' % str(err)
    logger.info('res data[%s]:(result=%s, info=%s)' % (request.path, result['ack_result']['status'], result['ack_result']['info']))
    return jsonify(result)

# 统一DELETE处理
@main.route('/<string:config_name>/<int:record_id>/', methods=['DELETE'])
def genral_delete(config_name, record_id):
    try:
        logger.info('request [POST:%s][para:%s]-->%s', request.path, request.args.to_dict(), request.json)
        if config_name.lower() in genral_config.keys():
            result = genral_config[config_name.lower()].deal_delete_method(request)
        else:
            result = json.loads(utilConfig.request_result)
            result['ack_result']['status'] = 'ERR'
            result['ack_result']['info'] = '未匹配到视图! [%s]' % config_name
    except Exception as err:
        result = json.loads(utilConfig.request_result)
        result['ack_result']['status'] = 'ERR'
        result['ack_result']['info'] = '未匹配到视图! [%s]' % str(err)
    logger.info('res data[%s]:(result=%s, info=%s)' % (request.path, result['ack_result']['status'], result['ack_result']['info']))
    return jsonify(result)


