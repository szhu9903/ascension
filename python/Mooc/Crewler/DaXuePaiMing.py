import requests
from bs4 import BeautifulSoup
import bs4


def get_msg(url):
    try:
        head = {'user-agent':'Mozilla/5.0'}
        response = requests.get(url,timeout=30,headers=head)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except Exception as er:
        print(er)
        return ''

def msg_extract(text,dx_list):
    try:
        response_text = BeautifulSoup(text,'html.parser')
        for tr in response_text.find('tbody').children:
            if isinstance(tr,bs4.element.Tag):
                td = tr.find_all('td')
                dx_list.append([td[0].string,td[1].string,td[3].string])
        return dx_list
    except Exception as er:
        print(er)
        return ''

def print_msg(dx_list):
    """
    格式化输出：
        <:左对齐
        ^:居中
        >:右对齐
        10:长度
        chr(12288):
    :param dx_list:
    :return:
    """
    try:
        print_format = '{0:^10}\t{1:{3}^10}\t{2:^10}'
        print(print_format.format('排名','大学名称','得分',chr(12288)))
        for i in dx_list and dx_list:
            print(print_format.format(i[0],i[1],i[2],chr(12288)))
    except Exception as er:
        print(er)
        return ''

def main():
    dx_list = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    r_text = get_msg(url)
    data = msg_extract(r_text,dx_list)
    print_msg(data)

if __name__ == '__main__':
    main()
