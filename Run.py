# -*- coding: utf-8 -*-
# @Time    : 18-7-7 下午7:16
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : Run.py
# @Software: PyCharm
from collections import Counter
if __name__ == '__main__':
    from HMY.Get_Data import Get_data
    X,y= Get_data('pc4.arff')
    from HMY.Resampling import Integrated_Sampling
    X_rabalance,y_rebalance = Integrated_Sampling(X,y,'FALSE','TRUE')
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X_rabalance, y_rebalance, test_size=0.3)
    #对训练集进行重采样
    print("【训练阶段：】")
    values_counts = Counter(y_train)
    print("训练集样本类别统计：", values_counts)
    values_counts = Counter(y_test)
    print("测试集样本类别统计：", values_counts)
    from HMY.CWsRF_V2 import CWsRF
    y_predict,y_test = CWsRF(X_train, X_test, y_train, y_test)
    from sklearn.metrics import classification_report,roc_auc_score
    print("【结果：】")
    print(classification_report(y_test,y_predict))
    print("AUC：",roc_auc_score(y_test,y_predict))
