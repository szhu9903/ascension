import requests

def baidu(url):
    kv = {'wd':'python'}
    # heard = {'user-agent':'Mozilla/5.0'}
    response_data = requests.get(url,params=kv,timeout=30)
    response_data.raise_for_status()
    print(response_data.headers,len(response_data.text))
    response_data.encoding = response_data.apparent_encoding
    return response_data.text[:100]


def get_ip(url,ip):
    try:
        kv = {'ip':ip,'action':'2'}
        heards = {'user-agent':'Mozilla/5.0'}
        response_data = requests.get(url,params=kv,timeout=30,headers=heards)
        response_data.raise_for_status()
        print(response_data.encoding)
        response_data.encoding = response_data.apparent_encoding
        return response_data.text
    except Exception as er:
        return 'error'


if __name__ == '__main__':
    # url = 'http://www.baidu.com/s'
    # print(baidu(url))

    url = 'https://www.ip138.com/iplookup.asp'
    ip = '192.168.2.237'
    print(get_ip(url,ip))