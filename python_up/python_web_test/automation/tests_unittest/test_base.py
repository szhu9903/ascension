
import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        print('test setup')

    def setUpClass(cls):
        print('test setUpClass')
    def test01_login(self):
        print('test loging01')
    def test02_login(self):
        print('test loging02')
    def tearDownClass(cls):
        print('test tearDownClass')
    def tearDown(self):
        print('test tearDown')
