import requests,re,os
from bs4 import BeautifulSoup

def get_img_url(url,path,index=1):
    try:
        head = {'user-agent':'Mozilla/5.0'}
        response = requests.get(url,timeout=30,headers=head)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        response_text = BeautifulSoup(response.text,'html.parser')
        for img in response_text.find_all(src=re.compile('wx')) :
            if index >100:
                return 'OK'
            else:
                img_url = 'http:'+img.get('src')
                print('开始下载第%s张图片'%index)
                download_img(img_url,path)
                index += 1
                print('完成')
        next_page = 'http:'+ response_text.find(title='Older Comments').get('href')
        get_img_url(next_page,path,index)

    except Exception as er:
        return '获取图片地址失败：%s'%er

def download_img(url,path):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        path_img = path+url.split('/')[-1]
        if not os.path.exists(path_img):
            read = {'user-agent':'Mozilla/5.0'}
            response = requests.get(url,timeout = 30,headers = read)
            response.raise_for_status()
            with open(path_img,'wb') as t:
                t.write(response.content)
                t.close()
        else:
            return '已存在该图片'
    except Exception as er:
        return '下载失败：%s'%er


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    path = 'E:\\jiandan\\'
    get_img_url(url,path)