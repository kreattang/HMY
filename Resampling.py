# -*- coding: utf-8 -*-
# @Time    : 18-7-7 下午6:38
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : Resampling.py
# @Software: PyCharm
import operator
def Integrated_Sampling(X,y,target,target1):
    print("【数据再平衡阶段：】")
    from collections import Counter
    values_counts = Counter(y)
    print("原始训练集类别统计：", values_counts)
    X_maj = []
    y_maj = []
    X_min = []
    y_min = []

    #分割大类和小类
    for i in range(len(y)):
        if operator.eq(y[i],target):
            X_maj.append(X[i])
            y_maj.append(y[i])
        else:
            X_min.append(X[i])
            y_min.append(y[i])
    IR = len(y_maj) / (len(y_min) + 1)
    print("不平衡率IR:",IR)

    #SMOTE
    a = int(len(y_maj)/((IR/4.0)*3))
    X_temp = X_min+X_maj[:a]
    y_temp = y_min+y_maj[:a]
    from imblearn.over_sampling import SMOTE
    X_resampled, y_resampled = SMOTE().fit_sample(X_temp, y_temp)
    values_counts = Counter(y_resampled)
    print("SMOTE后类别统计：", values_counts)


    #k-means欠采样
    b = int(len(X_min)*((IR/4.0)*3))
    from sklearn.cluster import KMeans
    kmeans_Undersampling = KMeans(n_clusters=b, random_state=0).fit(X_maj)

    #最终训练集
    X_final = []
    y_final = []
    for i in range(len(y_resampled)):
        if operator.eq(y_resampled[i],target1):
            X_final.append(X_resampled[i])
            y_final.append(target1)
    for i in kmeans_Undersampling.cluster_centers_:
        X_final.append(i)
        y_final.append(target)
    values_counts = Counter(y_final)
    print("k-means欠采样后样本类别统计：", values_counts)
    return X_final, y_final






if __name__ == '__main__':
    from HMY.Get_Data import Get_data
    X, y = Get_data()
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    # 对训练集进行重采样
    Integrated_Sampling(X_train,y_train,'N','Y')