import requests
from base import BaseTestCase

class BlogTest(BaseTestCase):

    def setUp(self):
        super(BlogTest, self).setUp()
        self.cookies = self.login().cookies
        self.url = 'http://'+self.path_url+'/api/zsj/main/%s/'

    def test01_zsjblogtype(self):
        url = self.url % 'zsjblogtype'
        response = requests.get(url,
                                     timeout=30,
                                     headers=self.headers)
        self.assertEqual(response.status_code, 401)
        response = requests.get(url,
                                     timeout=30,
                                     headers=self.headers,
                                     cookies=self.cookies)
        self.assertEqual(response.status_code, 200)

    def test01_zsjblog(self):
        url = self.url % 'zsjblog'
        response = requests.get(url,
                                     timeout=30,
                                     headers=self.headers)
        self.assertEqual(response.status_code, 401)
        response = requests.get(url,
                                     timeout=30,
                                     headers=self.headers,
                                     cookies=self.cookies)
        self.assertEqual(response.status_code, 200)



