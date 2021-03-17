
from flask import request
from flask import jsonify
from comm import utilConfig

def middle(app):
    @app.before_request
    def app_before():
        if request.method in ['PUT','POST','DELETE'] and 'application/json' != request.headers['CONTENT_TYPE'].lower():
            result = utilConfig.request_result
            result['ack_result']['status'] = 'ERR_CONTENT_TYPE'
            result['ack_result']['info'] = '请求内容格式错误'
            return jsonify(result)


