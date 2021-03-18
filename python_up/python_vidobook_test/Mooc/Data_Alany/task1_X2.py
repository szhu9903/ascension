
#利用就餐时间段的数据对学生在不同食堂的就餐情况进行聚类分析
import pandas as pd
path= r"E:\job\meal_data.csv"
data1 = pd.read_csv(path,encoding='gbk')
data1.drop(labels=['Unnamed: 0.1', 'Unnamed: 0'],axis=1,inplace=True)

#提取每个食堂的数据
Dept_data1 = data1.loc[(data1['Dept'].apply(lambda x: x in ['第一食堂'])), :]
Dept_data2 = data1.loc[(data1['Dept'].apply(lambda x: x in ['第二食堂'])), :]
Dept_data3 = data1.loc[(data1['Dept'].apply(lambda x: x in ['第三食堂'])), :]
Dept_data4 = data1.loc[(data1['Dept'].apply(lambda x: x in ['第四食堂'])), :]
Dept_data5 = data1.loc[(data1['Dept'].apply(lambda x: x in ['第五食堂'])), :]
#计算各个食堂的每人平均消费额
Dept_data1 = Dept_data1[['CardNo', 'Money']].groupby(by='CardNo').mean().reset_index()
Dept_data2 = Dept_data2[['CardNo', 'Money']].groupby(by='CardNo').mean().reset_index()
Dept_data3 = Dept_data3[['CardNo', 'Money']].groupby(by='CardNo').mean().reset_index()
Dept_data4 = Dept_data4[['CardNo', 'Money']].groupby(by='CardNo').mean().reset_index()
Dept_data5 = Dept_data5[['CardNo', 'Money']].groupby(by='CardNo').mean().reset_index()

#月就餐次数
month_count = data1[['CardNo', 'Money']].groupby(by='CardNo').count().reset_index()


#关联数据
features = pd.merge(Dept_data1, Dept_data2, on='CardNo', how='inner')
features = pd.merge(Dept_data3, features, on='CardNo', how='inner')
features = pd.merge(Dept_data4, features, on='CardNo', how='inner')
features = pd.merge(Dept_data5, features, on='CardNo', how='inner')
features = pd.merge(month_count, features, on='CardNo', how='inner')
features.columns = ['CardNo', '月就餐次数', '第五食堂每人平均消费额', '第四食堂每人平均消费额','第三食堂每人平均消费额', '第一食堂每人平均消费额', '第二食堂每人平均消费额']

# 标准化处理
from sklearn import preprocessing
data_pre = preprocessing.scale(features.iloc[:, 1:])

# 轮廓系数法确定聚类数
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
from matplotlib import pyplot as plt
silhouettteScore = []
for i in range(2, 8):
    kmeans1 = KMeans(n_clusters=i, random_state=123).fit(data_pre)
    score = silhouette_score(data_pre, kmeans1.labels_)
    silhouettteScore.append(score)
plt.subplot(2,1,1)
plt.figure(figsize=(6, 4))
plt.plot(range(2, 8), silhouettteScore, linewidth=1.5, linestyle="-")

# 构建Kmeans聚类模型
kmeans_model = KMeans(n_clusters=5, max_iter=100)
kmeans_model.fit(data_pre)
fit_label = kmeans_model.labels_
features['fit_label'] = fit_label
center = kmeans_model.cluster_centers_

#查看聚类效果 ：散点图
plt.rcParams['font.sans-serif'] = 'SimHei' 
plt.rcParams['axes.unicode_minus']=False
plt.subplot(2,1,2)
markers = ['D','v','+','*','o']
for i in range(5):
   plt.scatter(data_pre[fit_label == i, 0], data_pre[fit_label == i, 1],marker = markers[i])
plt.show()

