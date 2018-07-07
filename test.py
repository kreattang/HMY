# -*- coding: utf-8 -*-
# @Time    : 18-7-6 上午11:22
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : test.py
# @Software: PyCharm
from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

print(kmeans.cluster_centers_)