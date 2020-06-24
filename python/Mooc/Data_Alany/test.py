import matplotlib.pyplot as plt
import pandas as pd


def group_ct(path):
    try:
        f = open(path,encoding='gbk')
        data_4 = pd.read_csv(f)
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus']=False
        plt.figure(figsize=(5,5))
        count_num = data_4['Dept'].value_counts()


        plt.pie(count_num,autopct='%.2f %%',
                labels=['第一食堂','第二食堂','第三食堂','第四食堂','第五食堂'],
                shadow=False, startangle=90)
        plt.title('早餐就餐地点')
        plt.show()
        return True
    except Exception as er:
        print(er)



if __name__ == '__main__':
    path = './早餐.csv'
    path_group = group_ct(path)