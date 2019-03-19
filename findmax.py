"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-18, 17:07
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""
## 简单的递归思想

def findmax(arr):
    l = 0
    r = len(arr)-1
    #先写递归出口：
    if l == r:
        return arr[l]

    else:
        return max(arr[l],findmax(arr[l+1:]))




ans=findmax([1,7,0,6,-3])
print(ans)

