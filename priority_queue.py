#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# __author_: 米兰小子

import heapq

pqueue = []
heapq.heappush(pqueue, (1, 'A'))
heapq.heappush(pqueue, (7, "B"))
heapq.heappush(pqueue, (3, "C"))
heapq.heappush(pqueue, (6, "D"))
heapq.heappush(pqueue, (2, "E"))


# 从堆中逐个取出元素

while pqueue:
    print(heapq.heappop(pqueue))

# 堆的好处就是，每次从堆中弹出来的数，总是目前堆中最小的
#
#               |              |
#               |     4     34 |
#               |  1           |
#               | 3    9    5  |
#               |  18     20   |
#               |        10    |
#               |   39       0 |
#               ————————————————
#    每次执行heapq.heappop(q) 总是弹出当前堆中最小元素