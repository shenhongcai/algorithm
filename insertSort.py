"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-19, 10:52
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""

import timeit


def insertSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        index = i     # 每次遍历开始，都将游标指向当前元素(待比较）

        # 将要插入的元素与已经排好的子序列中的元素从后往前逐一比较，直到找到一个比待插入元素小的
        while arr[index-1] > current and index > 0:
            arr[index] = arr[index-1]
            index = index-1
        arr[index] = current
    return arr


if __name__ == "__main__":
    test = [9, 8, -3, 5, 13, 1, 2, -10, -12, 15]
    insertSort(test)
    time1 = timeit.Timer(stmt="insertSort(test),test", setup="from __main__ import insertSort, test")

    print("插入排序的时间:%s s" % time1.timeit(1))
    print(insertSort(test))

    # 使用lambda 推导
    print("插入排序的时间:%s s" % timeit.Timer(lambda: insertSort(test)).timeit(1))










