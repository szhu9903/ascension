import unittest
import time
from celery_demo.tasks import add_longtime

class CeleryTest(unittest.TestCase):
    def test_add(self):
        # 调用任务
        res = add_longtime.delay(4, 3)
        self.assertFalse(res.ready())
        # time.sleep(4)
        # self.assertTrue(res.ready())
        print(res.get())
        self.assertTrue(res.ready())

