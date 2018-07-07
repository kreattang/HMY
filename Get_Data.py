# -*- coding: utf-8 -*-
# @Time    : 18-6-20 下午3:51
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : Get_Data.py
# @Software: PyCharm

def Get_data(file_name):
    X = []
    # X = [[]*1 for i in range(5418)]
    Y = []
    with open(file_name, 'r') as fp:
        for line in fp.readlines():
            line = line.strip('\n')
            # print(line)
            if '?' not in line:
                temp = []
                T = line.split(',')
                for l in range(len(T)-1):
                    temp.append(float(T[l]))
                X.append(temp)
                Y.append(str(T[-1]))
    return X,Y





