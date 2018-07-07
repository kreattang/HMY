# -*- coding: utf-8 -*-
# @Time    : 18-7-6 上午11:19
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : Data_processing.py
# @Software: PyCharm
import operator
def Integrated_Sampling(X,y):
    print("【数据再平衡阶段：】")
    from collections import Counter
    values_counts = Counter(y)
    print("原始训练集类别统计：", values_counts)
    X1 = []
    X0 = []
    y1 = []
    y0 = []
    for i in range(len(y)):
        # print(operator.eq(y[i],'FALSE'))
        if operator.eq(y[i],'N')==True:
            X1.append(X[i])
            y1.append(y[i])
        else:
            X0.append(X[i])
            y0.append(y[i])
    from imblearn.over_sampling import SMOTE
    smote = SMOTE(random_state=0)
    IR = len(y1)/(len(y0)+1)
    # print("不平衡率IR:",IR)
    #计算SMOTE参数
    X_train = X0+X1[:int(IR/2.00*len(y0))]
    y_train = y0+y1[:int(IR/2.00*len(y0))]
    X_resampled, y_resampled = SMOTE().fit_sample(X_train, y_train)
    values_counts = Counter(y_resampled)
    print("SMOTE后类别统计：", values_counts)

    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=int(IR/1.500*len(y0)), random_state=0).fit(X1)
    # print("k-means欠采样后大类样本个数：",len(kmeans.cluster_centers_))
    X_final = []
    y_final = []
    for i in range(len(y_resampled)):
        if operator.eq(y_resampled[i],'Y')==True:
            X_final.append(X_resampled[i])
            y_final.append('Y')
    for i in kmeans.cluster_centers_:
        X_final.append(i)
        y_final.append('N')
    values_counts = Counter(y_final)
    print("k-means欠采样后样本类别统计：", values_counts)
    return X_final,y_final


def Data():
    from HMY.Get_Data import Get_data
    X,y = Get_data()
    #分割训练集和测试集
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    #数据再平衡
    X_train, y_train = Integrated_Sampling(X_train,y_train)
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = Data()