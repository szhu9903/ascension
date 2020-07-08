
import pandas as pd


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


if __name__ == '__main__':
    excel_path = r"E:\Stock\stock20200505210648.xls"
    # read_excel(excel_path)
    for i in read_excel(excel_path):
        print(i)