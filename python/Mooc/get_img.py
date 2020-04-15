import requests,os

def get_img(url,path):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        path_msg = path+url.split('/')[-1]
        if not os.path.exists(path_msg):
            kv = {'user-agent':'Mozilla/5.0'}
            response_data = requests.get(url,timeout=30,headers=kv)
            response_data.raise_for_status()
            with open(path_msg,'wb') as t:
                t.write(response_data.content)
                t.close()
        else:
            return '文件已存在'

    except Exception as er:
        print(er)
        return 'error'


if __name__ == '__main__':
    url = 'https://edu-image.nosdn.127.net/3321D6673EB82C94D08E1B80E8344166.jpg'
    path = 'E:\\jobs\\'
    get_img(url,path)