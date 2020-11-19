import time
import json
import logging
import requests

testLog = logging.getLogger('test')
testLog.setLevel(logging.DEBUG)
testHandle = logging.StreamHandler()
testFormatter = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", '%Y-%m-%d %H:%M:%S')
testHandle.setLevel(logging.DEBUG)
testHandle.setFormatter(testFormatter)
testLog.addHandler(testHandle)

logger = logging.getLogger('test')


request_json = {
    "req_info":{
        "data":{
            "si_phonenum" : '15977798889'
        }
    }
}


class RequestTest(object):
    # 初始化自动向登录接口获取cookies
    def __init__(self, module_name):
        self.url = "http://127.0.0.1:8005/api/v1.0/config/%s/"%module_name
        self.headers = {'user-agent':'Mozilla/5.0','Content-Type':'application/json'}
        self.cookies = self.login_response_data().cookies

    # GET 测试
    def get_response_data(self):
        response_data = requests.get(self.url,
                                     timeout = 30,
                                     headers = self.headers,
                                     cookies=self.cookies)
        response_data.raise_for_status()
        response_data.encoding = 'utf-8'
        res = response_data.json()
        return res

    # DELETE 测试
    def delete_response_data(self, del_id):
        del_url = self.url + str(del_id) + '/'
        response_data = requests.delete(url = del_url,
                                        timeout = 30,
                                        headers = self.headers,
                                        cookies=self.cookies)
        response_data.raise_for_status()
        response_data.encoding = 'utf-8'
        res = response_data.json()
        time.sleep(5)
        return res['ack_result']['status']

    # post 测试
    def post_response_data(self, data):
        response_data = requests.post(self.url,
                                      json = data,
                                      timeout = 30,
                                      headers = self.headers,
                                      cookies = self.cookies)
        response_data.raise_for_status()
        res = response_data.json()
        return res

    # PUT 测试
    def put_response_data(self, put_id, data = request_json):
        put_id = self.url + str(put_id) + '/'
        response_data = requests.put(put_id,
                                      json = data,
                                      timeout = 30,
                                      headers = self.headers,
                                      cookies = self.cookies)
        response_data.raise_for_status()
        res = response_data.json()
        # 延时请求
        time.sleep(5)
        return res

    # 初始登录
    def login_response_data(self):
        url = "http://127.0.0.1:8005/api/v1.0/commfunc/login/"
        post_data = {
            "req_info":{
                "data":{
                    "user_name": "hudeli",
                    "user_password": "12345",
                    "terminal_type": "APP",
                    "adid":1
                }
            }
        }
        response_data = requests.post(url,
                                      data = json.dumps(post_data),
                                      headers = self.headers)
        response_data.raise_for_status()
        response_data.encoding = 'utf-8'
        return response_data


if __name__ == '__main__':
    ratio = RequestTest('SysIccard')
    data = ratio.get_response_data()

    # 新增测试
    for i in range(30):
        iccard_num = str(time.time())[::-1].replace('.', '') + '%04d' % i
        request_json['req_info']['data']['si_cardnum'] = iccard_num
        res = ratio.post_response_data(request_json)
        if res['ack_result']['status'] == 'OK':
            logger.info('SUCCESS %s' % res['ack_result']['info'])
        else:
            logger.error('ERROR %s' % res['ack_result']['info'])
        time.sleep(10)

    # # 修改测试
    # if data['ack_result']['data']:
    #     id_list = [did['id'] for did in data['ack_result']['data']]
    #     for p in map(ratio.put_response_data, id_list):
    #         logger.info('PUT SUCCESS %s ' % p['ack_result']['status'])

    # # 删除测试
    # if data['ack_result']['data']:
    #     id_list = [data['id'] for data in data['ack_result']['data']]
    #     for result in map(ratio.delete_response_data,id_list):
    #         logger.info('DELETE SUCCESS %s' % result)