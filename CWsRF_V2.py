# -*- coding: utf-8 -*-
# @Time    : 18-7-7 下午5:31
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : CWsRF_V2.py
# @Software: PyCharm


from HMY.Data_processing import Data
from collections import Counter

def CWsRF(X_train, X_test, y_train, y_test):
    from sklearn import preprocessing
    #对y标签进行编码
    le = preprocessing.LabelEncoder()
    le.fit(y_train+y_test)
    y_train = le.transform(y_train)
    y_test = le.transform(y_test)

    # 第1个分类器
    from sklearn.ensemble import RandomForestClassifier
    clf1 = RandomForestClassifier()
    clf1.fit(X_train, y_train)
    Y_train_c1 = clf1.predict(X_train)
    Y_test_c1 = clf1.predict(X_test)

    # 第2个分类器
    from sklearn.svm import SVC
    clf2 = SVC()
    clf2.fit(X_train, y_train)
    Y_train_c2 = clf2.predict(X_train)
    Y_test_c2 = clf2.predict(X_test)

    # 第3个分类器
    from sklearn.ensemble import RandomForestClassifier
    clf3 = RandomForestClassifier()
    clf3.fit(X_train, y_train)
    Y_train_c3 = clf3.predict(X_train)
    Y_test_c3 = clf3.predict(X_test)

    Acc_1_min = Acc_1_maj = Acc_2_min = Acc_2_maj = Acc_3_min = Acc_3_maj = 0.0
    for i in range(len(Y_train_c1)):
        if Y_train_c1[i] == 0:
            Score = 0
            score = 3 - (Y_train_c1[i] + Y_train_c2[i] + Y_train_c3[i])
            if y_train[i] == Y_train_c1[i]:
                Score = 1 * score
            else:
                Score = 0 * score
            Acc_1_min = Acc_1_min + Score
        if Y_train_c1[i] == 1:
            Score = 0
            score = Y_train_c1[i] + Y_train_c2[i] + Y_train_c3[i]
            if y_train[i] == Y_train_c1[i]:
                Score = 1 * score
            else:
                Score = 0 * score
            Acc_1_maj = Acc_1_maj + Score
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
                Score = 1 * score
            else:
                Score = 0 * score
            Acc_2_maj = Acc_2_maj + Score
        if Y_train_c3[i] == 0:
            Score = 0
            score = 3 - (Y_train_c1[i] + Y_train_c2[i] + Y_train_c3[i])
            if y_train[i] == Y_train_c3[i]:
                Score = 1 * score
            else:
                Score = 0 * score
            Acc_3_min = Acc_3_min + Score
        if Y_train_c3[i] == 1:
            Score = 0
            score = Y_train_c1[i] + Y_train_c2[i] + Y_train_c3[i]
            if y_train[i] == Y_train_c3[i]:
                Score = 1 * score
            else:
                Score = 0 * score
            Acc_3_maj = Acc_3_maj + Score
    w_1_MIN = round(Acc_1_min / float(list(Y_train_c1).count(0)), 2)
    w_1_MAJ = round(Acc_1_maj / float(list(Y_train_c1).count(1)), 2)
    w_2_MIN = round(Acc_2_min / float(list(Y_train_c2).count(0)), 2)
    w_2_MAJ = round(Acc_2_maj / float(list(Y_train_c2).count(1)), 2)
    w_3_MIN = round(Acc_3_min / float(list(Y_train_c3).count(0)), 2)
    w_3_MAJ = round(Acc_3_maj / float(list(Y_train_c3).count(1)), 2)

    vtr1 = [y * w_1_MIN for y in Y_train_c1]
    vtr2 = [y * w_2_MIN for y in Y_train_c2]
    vtr3 = [y * w_3_MIN for y in Y_train_c3]
    vte1 = [y * w_1_MIN for y in Y_test_c1]
    vte2 = [y * w_2_MIN for y in Y_test_c2]
    vte3 = [y * w_3_MIN for y in Y_test_c3]
    vtrain = []
    for i in range(len(vtr1)):
        vtrain.append(round(vtr1[i] + vtr2[i] + vtr3[i], 2))
    vtest = []
    for i in range(len(vte1)):
        vtest.append(round(vte1[i] + vte2[i] + vte3[i], 2))
    vtr_new = []
    for i in vtrain:
        temp = []
        for j in range(1, 4):
            # print(i)
            if i > j:
                temp.append(1)
            else:
                temp.append(0)
        vtr_new.append(temp)
    vtr_new1 = vtr_new2 = vtr_new3 = []
    for i in range(len(vtr_new)):
        vtr_new1.append(vtr_new[i][0])
        vtr_new2.append(vtr_new[i][1])
        vtr_new3.append(vtr_new[i][2])
    j = max([AUC(vtr_new1), AUC(vtr_new2), AUC(vtr_new3)])
    result = []
    for i in vtest:
        if i > j:
            result.append(1)
        else:
            result.append(0)
    return result,y_test



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



