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


# 拿出来

while pqueue:
    print(heapq.heappop(pqueue))



