from bs4 import BeautifulSoup
import requests

def beautiful_test(url):
    try:
        heards = {'user-agent':'Mozilla/5.0'}
        response_data = requests.get(url,timeout=30,headers = heards)
        response_data.raise_for_status()
        response_data.encoding = response_data.apparent_encoding
        response_data_text = BeautifulSoup(response_data.text,'html.parser')
        tag = response_data_text.a
        tag_head = response_data_text.body
        """
        tag.attrs:标签类元素
        tag.name 标签名
        tag.string 标签内内容
        tag.comment 注释信息
        """
        """
        遍历方法
        下行遍历
            tag.contents 下级所有节点list
            tag.children 遍历下级节点
            tag.descendants 遍历下级所有
        上行遍历
            tag.parent 上级节点
            tag.parents 上级先辈节点
        平行遍历
            tag.previous_sibling 上一个节点
            tag.pervious_siblings 前面所有
            tag.next_sibling 下一个节点
            tag.next_siblings 后面所有节点
        """
        print(tag_head.contents[1])
        for i in tag_head.children:
            print(i)
        return response_data_text
    except Exception as er:
        return 'Error:%s'%er


if __name__ == '__main__':
    url = 'https://zsjblog.com/index'
    beautiful_test(url)

