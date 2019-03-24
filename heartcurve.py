"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-20, 01:46
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""

# -*- coding:utf8 -*-
# __author__ = 'wangxuhao'
# __file__ = 'Cardioid'

import matplotlib.pyplot as plt
import numpy as np
import math

t = np.linspace(0, math.pi, 1000)
x = np.sin(t)
y = np.cos(t) + np.power(x, 2.0 / 3)
plt.plot(x, y, color='red', linewidth=2)
plt.plot(-x, y, color='red', linewidth=2)
plt.title("heart")
plt.ylim(-2, 2)
plt.xlim(-2, 2)
plt.show()










