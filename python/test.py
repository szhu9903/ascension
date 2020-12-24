
import struct
import math
import logging
import datetime

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



if __name__ == '__main__':
    now_date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    date_list = now_date.split('-')
    msg_body_date = struct.pack('!H', int(date_list[0])) + \
                    struct.pack('!5B', int(date_list[1]), int(date_list[2]),
                                int(date_list[3]), int(date_list[4]), int(date_list[5]))
    print(msg_body_date)

    a = '121'
    print(a.split(','))

    # request_data = b'[GET / HTTP/1.1\r\nHost: localhost:9000\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'
    # print(request_data[0])
    # print(request_data[-1])
    # print(request_data[-2])
    # if request_data[0] == 0x5B:
    #     print('t')

    # s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
    # *str_data, a, b = struct.unpack('<20B2f', s[2:])
    # print(''.join(['%02X'%item for item in str_data]))
    # str_data = ''.join([str(item) for item in str_data])
    # print(str_data, a, b)
    # ver = 0
    #
    # version_all = '11.3'
    # print(version_all.split(','))
    #
    # if str(ver) != version_all.split(',')[0] and ver != 0:
    #     print('s')
    #
    # print('PRODUCECONTROL_MODIFYCONFIGRATIO_REQ'.lower())


    # 时间格式化
    time_minute = 307
    format_time = '%d:%02d' % (int(time_minute / 60), time_minute % 60)
    print(format_time)


    # 解析
    # data = b'C\xc5\xe33'
    # print(struct.pack('!f', 365.7749))
    #
    # main_version = struct.unpack('!f', data)
    # print(main_version)

    a = '(1048, "Column \'dsm_equipcode\' cannot be null")'
    if isinstance(a, str):
        print(a.replace('"', '\\"').replace("'", "\\'"))









