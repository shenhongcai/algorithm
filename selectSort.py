"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-19, 10:20
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""
import timeit


def selectSort(arr):

    n = len(arr)
    for i in range(n-1):    # 需要遍历 n-1 次
        for j in range(i,n):
            if arr[i]>arr[j]:
                arr[i], arr[j]=arr[j],arr[i]

    return arr


if __name__ == "__main__":
    test1 = [1, 0, -6, 7, 10, 17, 3, -19, 2,]
    test2 = [1, 2, 3, 4, 5]
    selectSort(test1)
    # 测量算法性能
    t1 = timeit.Timer("selectSort(test1),test1", setup="from __main__ import selectSort,test1")
    print("选择排序算法耗费时间:%s 秒" % t1.timeit(number=3))
    print(selectSort(test1))

"""
选择排序：
每遍历序列一次，只交换一次数据，即进行一次遍历时找到最大（最小）的项，完成遍历之后，把它交换到正确的
位置。第一次遍历后，最小（最大)的项已经归位，第二次遍历，使得次最小（最大）归位。
一共需要 n-1 次遍历来排好 n 个数据
"""





