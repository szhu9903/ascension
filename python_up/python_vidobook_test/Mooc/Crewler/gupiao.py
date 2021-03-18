import re,requests,traceback,os,datetime
from bs4 import BeautifulSoup
import xlwt

#下载页面通用方法
def getHTMLtext(url,code='utf-8'):
    headers = {'user-agent':'Mozilla/5.0'}
    response_data = requests.get(url,timeout=30,headers=headers)
    response_data.raise_for_status()
    response_data.encoding = code
    html = response_data.text
    return html

#获取所有公司股票代码列表
def getStockList(stock_list_url):
    try:
        html = getHTMLtext(stock_list_url)
        soup = BeautifulSoup(html, 'html.parser')
        a_list = soup.find_all('a')
        stock_list = []
        for i in a_list:
            try:
                msg = i.attrs['href']
                stock_list.append(re.search(r'[s][hz]\d{6}', msg)[0].upper())
            except Exception:
                continue
        return stock_list
    except:
        traceback.print_exc()

#遍历所有股票代码查询股票价格数据
def getStockInfo(stock_list,stock_msg_list,stockURL):
    count = 0
    error_list = []
    for dm in stock_list:
        try:
            url = stockURL+dm
            html = getHTMLtext(url)
            if html == '':
                continue
            stock_dict = {}
            soup = BeautifulSoup(html,'html.parser')
            stock_dict['stock_name'] = soup.find(attrs={'class':'stock-name'}).string
            stock_money = soup.find(attrs={'class':'stock-current'}).string
            stock_dict['stock_current'] = float(stock_money.replace('¥',''))
            stock_msg_list.append(stock_dict)
            count +=1
            print('\r当前获取个股成功进度{:.2f}%'.format(count*100/len(stock_list)),end='')
        except:
            error_list.append(dm)
    print('获取成功率{:.2f}%'.format(count*100/len(stock_list)))
    print('\r失败%s'%error_list)

#将所有股票信息写入本地excel文件
def setStockText(stock_msg_list,out_file):
    try:
        if not os.path.exists(out_file):
            os.makedirs(out_file)
        now_date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        path = out_file+'stock'+now_date+'.xls'
        work_book = xlwt.Workbook(encoding='utf-8')
        sheet = work_book.add_sheet('stock')
        t_head = {
            'stock_name':'股票名称',
            'stock_current':'股票价格'
        }
        head = ['stock_name','stock_current']
        stock_msg_list.insert(0,t_head)
        for row in range(len(stock_msg_list)):
            for col in range(len(head)):
                sheet.write(row,col,stock_msg_list[row][head[col]])
        work_book.save(path)
    except:
        traceback.print_exc()
        return ''

#主函数
def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stockURL = 'https://xueqiu.com/S/'
    out_file = 'E:\\Stock\\'
    stock_msg_list = []
    stock_list = getStockList(stock_list_url)
    getStockInfo(stock_list,stock_msg_list,stockURL)
    setStockText(stock_msg_list,out_file)


if __name__ == '__main__':
    main()
