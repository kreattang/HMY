# -*- coding: utf-8 -*-
# @Time    : 18-6-26 下午7:56
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : CWsRF.py
# @Software: PyCharm
from collections import Counter
from HMY.Data_processing import Data
X,y = Data()
print("【训练阶段：】")
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(y_train)

#训练集合样本类别统计
n_maj = list(y_train).count('N')
n_min = list(y_train).count('Y')


#第1个分类器
from sklearn.ensemble import RandomForestClassifier
clf1 = RandomForestClassifier()
clf1.fit(X_train,y_train)
y_predict_train_1 = clf1.predict(X_train)
y_predict_1 = clf1.predict(X_train)
y_predict_test_1 = clf1.predict(X_test)
Y_train_c1 = le.transform(list(y_predict_train_1))
Y_test_c1 = le.transform(list(y_predict_test_1))


#第2个分类器
from sklearn.svm import SVC
clf2 = SVC()
clf2.fit(X_train,y_train)
y_predict_train_2 = clf2.predict(X_train)
y_predict_2 = clf2.predict(X_train)
y_predict_test_2 = clf2.predict(X_test)
Y_train_c2 = le.transform(list(y_predict_train_2))
Y_test_c2 = le.transform(list(y_predict_test_2))



#第3个分类器
from sklearn.ensemble import RandomForestClassifier
clf3 = RandomForestClassifier()
clf3.fit(X_train,y_train)
y_predict_train_3 = clf3.predict(X_train)
y_predict_3 = clf3.predict(X_train)
y_predict_test_3 = clf3.predict(X_test)
Y_train_c3 = le.transform(list(y_predict_train_3))
Y_test_c3 = le.transform(list(y_predict_test_3))


y_train = le.transform(y_train)
y_test = le.transform(y_test)

Acc_1_min = Acc_1_maj = 0.0
Acc_2_min = Acc_2_maj = 0.0
Acc_3_min = Acc_3_maj = 0.0


# for i in range(list(Y_train_c1).count(1)):
for i in range(len(Y_train_c1)):
    if Y_train_c1[i] == 0:
        Score = 0
        score = 3-(Y_train_c1[i]+Y_train_c2[i]+Y_train_c3[i])
        if y_train[i] == Y_train_c1[i]:
            Score = 1*score
        else:
            Score = 0*score
        Acc_1_min = Acc_1_min+Score
    if Y_train_c1[i] == 1:
        Score = 0
        score = Y_train_c1[i]+Y_train_c2[i]+Y_train_c3[i]
        if y_train[i] == Y_train_c1[i]:
            Score = 1*score
        else:
            Score = 0*score
        Acc_1_maj = Acc_1_maj+Score
    if Y_train_c2[i] == 0:
        Score = 0
        score = 3 - (Y_train_c1[i] + Y_train_c2[i] + Y_train_c3[i])
        if y_train[i] == Y_train_c2[i]:
            Score = 1 * score
        else:
            Score = 0 * score
        Acc_2_min = Acc_2_min + Score
    if Y_train_c2[i] == 1:
        Score = 0
        score = Y_train_c1[i] + Y_train_c2[i] + Y_train_c3[i]
        if y_train[i] == Y_train_c2[i]:
            Score = 1*score
        else:
            Score = 0*score
        Acc_2_maj =Acc_2_maj+Score
    if Y_train_c3[i] == 0:
        Score = 0
        score = 3-(Y_train_c1[i]+Y_train_c2[i]+Y_train_c3[i])
        if y_train[i] == Y_train_c3[i]:
            Score = 1*score
        else:
            Score = 0*score
        Acc_3_min = Acc_3_min+Score
    if Y_train_c3[i] == 1:
        Score = 0
        score = Y_train_c1[i] + Y_train_c2[i] + Y_train_c3[i]
        if y_train[i] == Y_train_c3[i]:
            Score = 1 * score
        else:
            Score = 0 * score
        Acc_3_maj = Acc_3_maj + Score


w_1_MIN = round(float(Acc_1_min/list(Y_train_c1).count(0)),2)
w_1_MAJ = round(float(Acc_1_maj/list(Y_train_c1).count(1)),2)
w_2_MIN = round(float(Acc_2_min/list(Y_train_c2).count(0)),2)
w_2_MAJ = round(float(Acc_2_maj/list(Y_train_c2).count(1)),2)
w_3_MIN = round(float(Acc_3_min/list(Y_train_c3).count(0)),2)
w_3_MAJ = round(float(Acc_3_maj/list(Y_train_c3).count(1)),2)


vtr1 = [y*w_1_MIN for y in Y_train_c1]
vtr2 = [y*w_2_MIN for y in Y_train_c2]
vtr3 = [y*w_3_MIN for y in Y_train_c3]
vte1 = [y*w_1_MIN for y in Y_test_c1]
vte2 = [y*w_2_MIN for y in Y_test_c2]
vte3 = [y*w_3_MIN for y in Y_test_c3]


# print(Y_train_c1)
# print(y_train)
# print(vte1)
# print(vte2)
# print(vte3)

vtrain = []
for i in range(len(vtr1)):
    vtrain.append(round(vtr1[i]+vtr2[i]+vtr3[i],2))
vtest = []
for i in range(len(vte1)):
    vtest.append(round(vte1[i]+vte2[i]+vte3[i],2))
# print("vtrain:",vtrain)
# print(vtest)

def AUC(data):
    n_min = list(data).count(1)
    n_maj = list(data).count(0)
    ri = 0
    for i in range(len(data)):
        if data[i]==1:
            # print(i)
            ri = ri + int(i+1)
    # print(ri)
    AUC = (ri-n_min*(n_maj+1)/2)/float(n_min*n_maj)
    return AUC
# print(AUC(Y_train_c1),AUC(Y_train_c2),AUC(Y_train_c3))
# j = max([AUC(Y_train_c1),AUC(Y_train_c2),AUC(Y_train_c3)])
# print("j:",round(j,2))

vtr_new = []
for i in vtrain:
    temp = []
    for j in range(1,4):
        # print(i)
        if i>j:
            temp.append(1)
        else:
            temp.append(0)
    vtr_new.append(temp)
vtr_new1 = vtr_new2 = vtr_new3 = []
for i in range(len(vtr_new)):
    vtr_new1.append(vtr_new[i][0])
    vtr_new2.append(vtr_new[i][1])
    vtr_new3.append(vtr_new[i][2])
# print(vtr_new)
# print(vtrain)
# print(vtr_new)


j = max([AUC(vtr_new1),AUC(vtr_new2),AUC(vtr_new3)])

result = []
for i in vtest:
    if i > j :
        result.append(1)
    else:
        result.append(0)
# print(result)

# print(result)

from sklearn.metrics import classification_report,roc_auc_score
print(classification_report(result,y_test))
from sklearn.metrics import roc_auc_score
print("AUC",roc_auc_score(result,y_test))




