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

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    # print(get_url(url))
    print(post_url(url))