import requests

def get_url(url):
    try:
        respons_head = requests.head(url,timeout=30)
        print(respons_head.headers)
        respons = requests.get(url,timeout=30)
        respons.raise_for_status()
        respons.encoding = respons.apparent_encoding
        return respons.text
    except Exception as er:
        print(er)
        return '请求失败'

def post_url(url):
    try:
        data = {'ID':'123','UserName':'Szhu'}
        r = requests.post(url,data=data)
        r.raise_for_status()
        return r.text
    except Exception as er:
        return er

def get_jd_goods(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        respons_data = requests.get(url,timeout=30,headers=kv)
        respons_data.raise_for_status()

        print(respons_data.status_code,respons_data.headers,respons_data.encoding,respons_data.apparent_encoding)
        # respons_data.encoding = respons_data.apparent_encoding

        return respons_data.text
    except Exception as er:
        print(er)
        return '请求失败'


if __name__ == '__main__':
    # url = 'http://httpbin.org/post'
    # print(get_url(url))
    # print(post_url(url))
    # JD
    url = 'https://item.yhd.com/13758141430.html'
    print(get_jd_goods(url))