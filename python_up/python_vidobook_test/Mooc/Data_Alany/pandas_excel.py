import pandas as pd
import traceback

def load_excel(path):
    try:
        data = pd.read_excel(path,sheet_name=0,names=['name','all_name','num'])
        records = pd.DataFrame(data).to_dict(orient='records')
    except:
        traceback.print_exc()


if __name__ == '__main__':
    excel_path = r'F:\合盛硅业\06-基础资料\20200509合盛部门信息.xlsx'
    load_excel(excel_path)

