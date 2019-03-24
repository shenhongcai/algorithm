"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-23, 00:16
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""
import sys


def list2str(li):
    while li[0] == 0:
        del li[0]
    res = ''
    for i in li:
        res += str(i)
    return res


def multi(stra, strb):
    aa = list(stra)
    bb = list(strb)
    lena = len(stra)
    lenb = len(strb)
    result = [0 for i in range(lena + lenb)]
    for i in range(lena):
        for j in range(lenb):
            result[lena - i - 1 + lenb - j - 1] += int(aa[i]) * int(bb[j])
    for i in range(len(result) - 1):
        if result[i] >= 10:
            result[i + 1] += result[i] // 10
            result[i] = result[i] % 10
    return list2str(result[::-1])


if __name__ == '__main__':
    #s = "72106547548473106236 982161082972751393"
    s="22 33"
    s1 = s.split()[0]
    s2 = s.split()[1]
    ans=multi(s1,s2)
    print(ans)












