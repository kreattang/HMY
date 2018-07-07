# -*- coding: utf-8 -*-
# @Time    : 18-6-22 上午9:41
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : Weight.py
# @Software: PyCharm
import re
def Weight(maj,min):
    with open('DT.dot', 'r') as fp:
        temp = ''
        for line in fp.readlines():
            line = line.strip('\n')
            temp = temp + line
        pattern = re.compile(r'\[\d+, \d+\]')  # 查找数字
        result1 = pattern.findall(temp)
        result2 = []
        for r in result1:
            if ', 0]' not in r:
                if '[0, ' not in r:
                    # print(r)
                    result2.append(r)
        # print(result2)
        pattern = re.compile(r'\d+')  # 查找数字
        result3 = pattern.findall(str(result2))
        # print(result3)
        sum = 0
        oushu = 0
        jishu = 0
        for i in range(len(result3)):
            sum = sum + int(result3[i])
            if i % 2 == 0:
                oushu = oushu + int(result3[i])
            else:
                jishu = jishu + int(result3[i])
        maj_sup = oushu / float(sum)
        min_sup = jishu / float(sum)
        # print(maj_sup,min_sup)
        wmaj = (1-maj/float(maj+min))/maj_sup
        wmin = (1-min/float(maj+min))/min_sup
        # print(wmaj,wmin)
        return wmaj,wmin
# Weight(226,27)




