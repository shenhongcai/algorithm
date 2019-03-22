"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-22, 15:51
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""


## 更相减损术，求最大公约数

def gcd(a, b):

    if a-b == 0:
        print("最大公约数为：%d" % a)
        return a
    else:
        return gcd(b, abs(a - b))


gcd(20, 15)

"""
            20-15=10
            15-10=5
            10-5=5
            5-5=0
            return :5



"""









