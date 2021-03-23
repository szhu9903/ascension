import os
import struct
import math
import logging
import datetime
import re

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


def numInteraction(num1, num2, res=[]):
    # return list(set(num1) & set(num2))
    [res.append(n) for n in num1 if n in num2 and n not in res]
    return res

def vehicle_list(num1,num2):
    # num1中存在，num2中不存在-->删除num1中元素
    new_num1 = [n1 for n1 in num1 if n1 in num2]
    print(list(new_num1))
    # num1中不存在，num2中存在-->获取num2
    new_num2 = [n2 for n2 in num2 if n2 not in new_num1]
    print(new_num2)
    # 合并
    return new_num1 + new_num2

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

"""
def lengthOfLongestSubstring(s):
    if len(s) <= 0:return 0
    max_str = ''
    max_len = 0
    for i in s:
        if i in max_str:
            max_str = max_str[max_str.index(i)+1:]
        max_str += i
        if max_len < len(max_str):max_len=len(max_str)
    return max_len

def get_bytes_str(str_data, split_num, data_list):
    if split_num <= 0:
        return data_list, str_data
    else:
        res_index = str_data.index('0')
        res = str_data[:res_index]
        data_list.append(res)
        return get_bytes_str(str_data[res_index + 1:], split_num-1, data_list)

if __name__ == '__main__':
    # now_date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # date_list = now_date.split('-')
    # msg_body_date = struct.pack('!H', int(date_list[0])) + \
    #                 struct.pack('!5B', int(date_list[1]), int(date_list[2]),
    #                             int(date_list[3]), int(date_list[4]), int(date_list[5]))
    # print(msg_body_date)

    data_list,data_str = get_bytes_str('aaaaaa0fffffsefv0sdffgwed0fgwegewrf0cddsdffsdfgsdfsdf0sdgsdfsdf0sdf', 2, [])

    # # 文件读取编码
    # import struct
    # file_path = r'F:\砼秘书\szhu\VehicleMainCtrl_02.2.bin'
    # # file_path = r'F:\砼秘书\szhu\问题记录.txt'
    # with open(file_path, 'rb') as f:
    #     f_data = f.read()
    # print(f_data[:512])
    #
    # new_str = struct.pack('!512p', f_data[:512])
    # print(new_str)
    # print(new_str)



    import math
    # 向上取整
    print(math.ceil(513/512))


    import re
    # 替换adid的值
    st = 'kfklfpdsCfsC3a555afs'.upper()
    b = re.search(r'C\d{2}',st)
    if b:
        print(b.group())
    else:
        print('ssssssss')

    # print(datetime.datetime.now().date())
    # print(datetime.datetime.now().strftime('%Y-%m-%d'))
    #
    #
    # a = '请12001号车进入1号生产线,18000号车准备'
    # b = a.encode('GB2312') + bytes([0])
    # print(b)
    #
    # res = lengthOfLongestSubstring(' nnnko')
    # print(res)

    # # 时间格式化
    # time_minute = 307
    # format_time = '%d:%02d' % (int(time_minute / 60), time_minute % 60)
    # print(format_time)










