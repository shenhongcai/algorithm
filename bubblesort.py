"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-18, 17:37
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""
import timeit


def bubblesort(arr):
    l = 0
    r = len(arr) - 1
    exchange = False
    if l == r:
        return arr[0]
    while l < r:
        for i in range(l, r - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                exchange = True

        if not exchange:
            break
        r = r-1
    return arr


def isSorted(arr):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


if __name__ == "__main__":
    test1 = [1, 0, -6, 7, 10]
    test2 = [1, 2, 3, 4, 5]
    bubblesort(test1)

    t1 = timeit.Timer("bubblesort(test1),test1", setup="from __main__ import bubblesort,test1")
    print("冒泡算法耗费时间:%s s" % t1.timeit(number=10))
    print(bubblesort(test1))









