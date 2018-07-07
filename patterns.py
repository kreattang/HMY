# -*- coding: utf-8 -*-
# @Time    : 18-6-19 下午9:15
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : patterns.py
# @Software: PyCharm




def pattern(X):
    class1 = 0
    class2 = 0
    def add(c1, c2, value1, value2):
        c1 = c1 + value1 / float(value1 + value2)
        c2 = c2 + value2 / float(value1 + value2)
        return c1,c2
    if X[28] <= 47.0: class1,class2=add(class1,class2,159,18)
    if X[28] > 47.0 and X[2] <=13.5:class1,class2=add(class1,class2,10,9)
    if X[28] > 47.0 and X[2] <=13.5 and X[24] <= 1574.76:class1,class2=add(class1,class2,10,4)
    if X[28] > 47.0 and X[2] <=13.5 and X[24] <= 1574.76 and X[32]<=47.0:class1,class2=add(class1,class2,3,4)
    if X[28] <=47.0 and X[17] <= 103.715:class1,class2=add(class1,class2,149,9)
    if X[28] <=47.0 and X[17] > 103.715 and X[6]<=4.5:class1,class2=add(class1,class2,149,9)
    if X[28] <=47.0 and X[17] <= 103.715 and X[7]<=0.125:class1,class2=add(class1,class2,148,8)
    if X[28] <=47.0 and X[17] <= 103.715 and X[7]<=0.125 and X[4]<= 15.5:class1,class2=add(class1,class2,17,3)
    if X[28] <=47.0 and X[17] <= 103.715 and X[7]>0.125 and X[0]<= 2.5:class1,class2=add(class1,class2,131,5)
    if X[28] <= 47.0 and X[17] <= 103.715 and X[7] <= 0.125 and X[4] <= 15.5 and X[0]<=4.5: class1,class2=add(class1, class2, 17, 2)
    if X[28] <= 47.0 and X[17] <= 103.715 and X[7] > 0.125 and X[0] <= 2.5 and X[17]<=28.59: class1,class2=add(class1, class2, 38, 5)
    return class1,class2
