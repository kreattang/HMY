# -*- coding: utf-8 -*-
# @Time    : 18-6-21 下午8:04
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : Data.py
# @Software: PyCharm
from HMY.Get_Data import Get_data
X,y = Get_data()
from collections import Counter
values_counts = Counter(y)
print("数据集样本类别统计：",values_counts)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
values_counts = Counter(y_train)
print("训练集样本类别统计：",values_counts)
values_counts = Counter(y_test)
print("测试集样本类别统计：",values_counts)
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
# from sklearn.neural_network import MLPClassifier
# clf1 = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(37,10), random_state=1)
clf1 = DecisionTreeClassifier(max_depth=5)
clf1.fit(X_train,y_train)
y_predict = clf1.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test,y_predict))
from sklearn import tree
from sklearn.externals.six import StringIO
dot_data = StringIO()
import pydot
tree.export_graphviz(clf1, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_dot('DT.dot')
graph[0].write_png('DT.png')

