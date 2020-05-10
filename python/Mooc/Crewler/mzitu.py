import requests,traceback,re,os,random
from bs4 import BeautifulSoup

def requests_url(url):
    referer = random.randint(1,30)
    headers = {'user-agent':'Mozilla/5.0','Referer':str(referer)}
    response_data = requests.get(url,timeout=30,headers=headers)
    response_data.raise_for_status()
    response_data.encoding = response_data.apparent_encoding
    return response_data

def url_list(url):
    try:
        rsps = requests_url(url)
        response_data = BeautifulSoup(rsps.text,'lxml')
        for p_msg in response_data.find_all(class_='url')[:2]:
            for a_msg in p_msg.find_all(target='_blank'):
                 yield a_msg.get('href'),a_msg.string
    except:
        traceback.print_exc()

def get_url_img(img_url,path,img_name):

    img_text = requests_url(img_url)
    response_data = BeautifulSoup(img_text.text,'lxml')
    img_donwload = response_data.find(src=re.compile(r'https://i3.mmzz')).get('src')
    response_img = requests_url(img_donwload)
    #下载到本地
    img_path = path+img_name+img_donwload.split('/')[-1]
    if not os.path.exists(img_path):
        with open(img_path,'wb') as f:
            f.write(response_img.content)
            f.close()


def main():
    url = 'https://www.mzitu.com/all/'
    path = 'E:\\mzitu\\'
    if not os.path.exists(path):
        os.makedirs(path)
    for img_list in url_list(url):
        try:
            count = 0
            print('\r开始下载%s'%img_list[1])
            while True:
                count += 1
                img_url = img_list[0]+'/'+str(count)
                get_url_img(img_url,path,img_list[1])
        except:
            continue


if __name__ == '__main__':
    main()
