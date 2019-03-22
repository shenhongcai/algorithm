"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-21, 09:22
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""
# 不使用“+”来求两个数的和


def newadd(a, b):
      ta = a&b
      tb = a^b
      while(ta):
            t_a = tb
            t_b = ta<<1
            ta = t_a & t_b
            tb = t_a ^ t_b
      print('a+b=', tb)

if __name__ == "__main__":
      newadd(4,5)









