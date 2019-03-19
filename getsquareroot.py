"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-20, 00:12
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""
# 牛顿法求一个数的平方根（square root)
import sys


def squareroot(x, precision):

    if x < 0:
        print("Tips: Invalid Value")
        return False
    elif x < 1:
        guess = x
        diff = sys.maxsize
        while diff > precision:
            ave = (x/guess+guess)/2
            diff = abs(ave-guess)
            guess = ave
        return guess
    else:
        guess = x/2
        diff = sys.maxsize
        while diff > precision:
            ave = (x / guess + guess) / 2
            diff = abs(ave - guess)
            guess = ave

        return guess


ans = squareroot(48, 0.0001)
print(ans)


"""
example: 求2的平方根 猜测为1(这么猜测是因为，对于大于1的数，其2倍小于它的平方，
        猜测为它的一半，更接近它的平方根）

        猜测(guess)          商(quotient)             平均值(ave)
           1                    2/1=2                (1+2)/2=1.5
           1.5                2/1.5=1.3333         (1.5+1.3333)/2=1.4167
           1.4167           2/1.4167=1.4118        (1.4167+1.4118)/2=1.4142
        1.4142                  ...                     ...
            ...                 ...                     ...


"""




















