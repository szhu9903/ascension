import requests, json

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
        return res['ack_result']['status']

    # 初始登录
    def login_response_data(self):
        url = "http://127.0.0.1:8005/api/v1.0/commfunc/login/"
        post_data = {
            "req_info":{
                "data":{
                    "user_name": "",
                    "user_password": "",
                    "terminal_type": "",
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
    ratio = RequestTest('ConfigRatio')
    data = ratio.get_response_data()
    result = None
    if data['ack_result']['data']:
        id_list = [data['id'] for data in data['ack_result']['data']]
        result = list(map(ratio.delete_response_data,id_list))
    print(result)