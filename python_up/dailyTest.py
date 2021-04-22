import os
import struct
import unittest
import logging
import re
import threading

# 添加日志设置等级，
logger = logging.getLogger('logName')
logger.setLevel(logging.DEBUG)
# 设置Handle, 在Handle中配置日志输出格式
loggerHandle = logging.StreamHandler()
# 注意日志格式设置中时间，是","号隔开的
loggerFormatter = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", '%Y-%m-%d %H:%M:%S')
loggerHandle.setLevel(logging.DEBUG)
loggerHandle.setFormatter(loggerFormatter)
# 将设置好的Handle添加进设置的日志中
logger.addHandler(loggerHandle)

thread_data = threading.local()


class DailyTest(unittest.TestCase):
    def setUp(self):
        logger.info('start test...')

    def test_str_split(self):
        data_str = b'\x00C35\x0011\xc2\xb111\x0011\xc2\xb111\x00\x0011\xc2\xb111\x00\x0011\xc2\xb111\x00'
        res_list, data_str = self.get_bytes_str(data_str, 5, [])
        print(res_list, data_str)

    def test_re_C30(self):
        st = 'kfklfpdsCfsC35555afs'.upper()
        b = re.search(r'C\d{2}', st)
        self.assertIsNotNone(b)
        print(b.group())

    def test_local(self):
        test_list = [3, 6, 9, 8, 5, 2, 1, 4, 7]
        test_list.sort()
        print(test_list)
    

    def get_bytes_str(self, data_str, split_num, data_list):
        if split_num <= 0:
            return data_list,data_str
        else:
            res_index = data_str.index(bytes([0]))
            res = data_str[:res_index].decode('utf-8')
            data_list.append(res)
            return self.get_bytes_str(data_str[res_index + 1:], split_num-1, data_list)







