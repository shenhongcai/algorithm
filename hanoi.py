"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-18, 16:41
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""
# 汉诺塔问题
# 递归思想


def hanoi(n, A, B, C):   # A, B, C 为三个柱子， n为盘子的数量
    if n == 1:
        print("{0}--->{1}".format(A, C))
    else:
        hanoi(n-1, A, C, B)
        print("{0}--->{1}".format(A, C))
        hanoi(n-1, B, A, C)


hanoi(3, "A", "B", "C")






