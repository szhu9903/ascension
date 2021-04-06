import time
import unittest
import threading

class ThreadTest(unittest.TestCase):
    def setUp(self):
        self.thread_data = threading.local()   # 线程局部变量，可用来记录线程中的数据库连接

    def test_theradlocal(self):
        thread1 = threading.Thread(target = self.get_therad_data, args=(5, 'threading1', ))
        thread2 = threading.Thread(target = self.get_therad_data, args=(2, 'threading2', ))
        thread1.start()
        thread2.start()


    def get_therad_data(self, time_len, thread_data):
        self.thread_data.loc_data = thread_data
        time.sleep(time_len)
        print(self.thread_data.loc_data)