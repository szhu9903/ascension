import pandas as pd
import time
import functools

# 时间消耗装饰器
def seep_date(func):
    @functools.wraps(func)
    def run_date(*args,**kwargs):
        start_date = time.time()
        rs = func(*args,**kwargs)
        end_date = time.time()
        print(end_date-start_date)
        return rs
    return run_date

def read_excel(path):
    try:
        data = pd.read_excel(path,sheet_name=0,names=['gp_name','gp_value'],
                             converters={'gp_name':str,'gp_value':float})
        records = data.to_dict('records')
        for record in records:
            if record['gp_value']>=3:
                yield record
    except Exception as er:
        print(er)

@seep_date
def main():
    excel_path = r"E:\Stock\stock20200505210648.xls"
    # read_excel(excel_path)
    for i in read_excel(excel_path):
        print(i)

if __name__ == '__main__':
    main()

