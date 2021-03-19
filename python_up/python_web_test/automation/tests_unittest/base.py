
import unittest
import json
import requests

req_data = {
    "req_info":{
        "data":None
    }
}

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.path_url = "127.0.0.1:8888"
        self.headers = {'user-agent':'Mozilla/5.0','Content-Type':'application/json'}
        self.req_data = req_data
        self.cookies = None

    def login(self, user_name=None, user_pwd=None):
        if user_name is None and user_pwd is None:
            user_name = 'admin'
            user_pwd = 'admin'
        self.req_data['req_info']['data'] = dict(user_name = user_name, user_pwd = user_pwd)
        url = 'http://%s/api/zsj/user/login/' % self.path_url
        response = requests.post(url,
                                 data=json.dumps(self.req_data),
                                 headers=self.headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response

    def logout(self):
        url = 'http://%s/api/zsj/user/logout/' %self.path_url
        requests.get(url, self.headers)


    def tearDown(self):
        self.cookies = None
