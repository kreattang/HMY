# -*- coding: utf-8 -*-
# @Time    : 18-7-2 下午8:55
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : RF.py
# @Software: PyCharm
from HMY.Get_Data import Get_data
from sklearn.model_selection import train_test_split
X,y = Get_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
from sklearn.metrics import confusion_matrix,classification_report,roc_auc_score
print(confusion_matrix(y_pred,y_test))
print(classification_report(y_pred,y_test))
