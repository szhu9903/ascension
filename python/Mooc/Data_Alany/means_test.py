import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import traceback

def get_pd(path):
    try:
        loan_data = pd.read_csv(path,encoding='gb18030')
        # 数据预处理
        where_data = loan_data[loan_data['Type'] == '消费']
        loan = where_data.groupby(['Major','Dept'])
        data_nan = loan['Money'].mean().unstack()
        loan_data = data_nan.fillna(0)
        loan_data['sum'] = loan_data.apply(lambda x: x.sum(),axis=1)
        data_col = list(loan_data._stat_axis.values.tolist())
        loan_data['indexs'] = data_col

        # 设置要进行聚类的字段
        loan_sum = np.array(loan_data[['sum']])

        estimator = KMeans(n_clusters=3)
        estimator.fit_predict(loan_sum)
        loan_data['labels'] = estimator.labels_
        print(estimator.cluster_centers_)
        print(loan_data.columns)

        # 提取不同类别的数据
        loan_data0 = loan_data.loc[loan_data["labels"] == 0]
        loan_data1 = loan_data.loc[loan_data["labels"] == 1]
        loan_data2 = loan_data.loc[loan_data["labels"] == 2]

        # 绘制聚类结果的散点图
        plt.rc('font', family='STXihei', size=10)
        plt.subplot(2, 1, 1)
        plt.scatter(loan_data0['indexs'],loan_data0['sum'], 50, color='#99CC01', marker='+', linewidth=2,
                    alpha=0.8)

        plt.scatter(loan_data1['indexs'], loan_data1['sum'], 50, color='#FE0000', marker='+', linewidth=2,
                    alpha=0.8)
        plt.scatter(loan_data2['indexs'], loan_data2['sum'], 50, color='#0000FE', marker='+', linewidth=2,
                    alpha=0.8)

        plt.xlabel('系')
        plt.ylabel('平均消费')

        plt.xlim(0,41)
        plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='both', alpha=0.4)

        # 绘制聚类结果的散点图
        plt.rc('font', family='STXihei', size=10)
        plt.subplot(2, 1, 2)
        plt.scatter(loan_data0['sum'], loan_data0['sum'], 50, color='#99CC01', marker='+', linewidth=2,
                    alpha=0.8)

        plt.scatter(loan_data1['sum'], loan_data1['sum'], 50, color='#FE0000', marker='+', linewidth=2,
                    alpha=0.8)
        plt.scatter(loan_data2['sum'], loan_data2['sum'], 50, color='#0000FE', marker='+', linewidth=2,
                    alpha=0.8)

        plt.xlabel('test_sum')
        plt.ylabel('平均消费')

        plt.xlim(0, 1000)
        plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='both', alpha=0.4)


        plt.show()


    except:
        traceback.print_exc()


if __name__ == '__main__':
    path = r"E:\job\task.csv"
    get_pd(path)