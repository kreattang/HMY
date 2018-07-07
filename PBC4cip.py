# -*- coding: utf-8 -*-
# @Time    : 18-6-22 上午9:44
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : PBC4cip.py
# @Software: PyCharm

from HMY.Get_Data import Get_data
from HMY.patterns import pattern
from HMY.Weight import Weight
X,y = Get_data()
from collections import Counter
values_counts = Counter(y)
print("数据集样本类别统计：",values_counts)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9)
values_counts = Counter(y_train)
print("训练集样本类别统计：",values_counts)
values_counts = Counter(y_test)
print("测试集样本类别统计：",values_counts)
Weight = Weight(226,27)
print("大类和小类的权值",Weight)
y_predict = []
for x in X_test:
    Support = pattern(x)
    # print("大类、小类支持度:",Support)
    if Weight[1]*Support[1] > Weight[0]*Support[0]:
        y_predict.append('Y')
    else:
        y_predict.append('N')
from  sklearn.metrics import confusion_matrix,classification_report
print(classification_report(y_test,y_predict))

