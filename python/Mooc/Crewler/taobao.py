import re,requests
from bs4 import BeautifulSoup

#抓取页面
def getHTMLtext(url):
    try:
        cookie = 'thw=cn; v=0; cna=/h4xFzQoFlcCAXrutXTQ7v4X; cookie2=1eab6b6ef3bfc72b0a39ef9e34497acb; t=63912b2b6b38bbd463debd03e66430a1; _tb_token_=f4e138773316e; _samesite_flag_=true; sgcookie=EG4bz6stuykys%2FfU58kxx; uc3=id2=UU8INVfV05iXKA%3D%3D&nk2=EuQDb%2FMWJ20xrDkNag%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dBxGR%2FhGGFjMFEnso%3D; csg=aa1542e7; lgc=qqabcd1017zsj; dnk=qqabcd1017zsj; skt=70c13964bc21b992; existShop=MTU4ODI1NjE4OA%3D%3D; uc4=nk4=0%40EJugT4tkJ2pvKMy8WXBfc7MIC2DdNh0l&id4=0%40U22PEF4vjXT2Y5VKTbzY%2FS4BsrOJ; tracknick=qqabcd1017zsj; _cc_=URm48syIZQ%3D%3D; enc=G7pygsNVQY2Mb4vNoPDfw0nsNLwQkraRAPKzGd04rS2oj1D9oEtD7L7Xd1N%2BlHLzXPahr5aMCvoKSLImy16vug%3D%3D; tfstk=c4tFBgawxDnEcmi9kMIPdGQWzF7dZM5lGlWV-EkJWkN0Hi7hiENRImX5QT5xjwf..; mt=ci=1_1; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTUMtULZeDd%2FA%3D%3D; JSESSIONID=65C4D8061079CBD341A258CB5ED0A38A; isg=BMHBPRZ1e79WzpeOTmB_Eb040A3b7jXg_bTmHCMX_0gnCuPcajoTsKtI6H5MBc0Y; l=eBLi8LKgQnpySmq9BO5anurza779EIObz1PzaNbMiIHca6sl9F1wfNQcx4yXWdtjgtfb3eKyKfwxsRn6Pizdg2HvCbKrCyCkFY9w-'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36ip'
        headers = {'user-agent':user_agent,'cookie':cookie}
        response_data = requests.get(url,timeout=30,headers=headers)
        response_data.raise_for_status()
        response_data.encoding = response_data.apparent_encoding
        return response_data.text
    except Exception as er:
        print(er)
        return ''

#解析页面信息
def parseHTML(infoList,html):
    try:
        plt = re.findall(r'"view_price":"[\d\.]*"',html)
        tlt = re.findall(r'"raw_title":".*?"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            infoList.append([price,title])
    except Exception as er:
        print(er)
        return ''

#打印解析到的信息
def printData(infoList):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format('序号','价格','名称'))
    count = 0
    for i in infoList:
        count+=1
        print(tplt.format(count,i[0],i[1]))

#主函数
def main():
    search_msg = input('输入名称：')
    page = 2
    infoList = []
    taobao_search = 'https://s.taobao.com/search?q='+search_msg
    for i in range(page):
        try:
            url = taobao_search+'&s='+str(i*44)
            html = getHTMLtext(url)
            parseHTML(infoList,html)
        except Exception:
            continue
    printData(infoList)


if __name__ == '__main__':
    main()
