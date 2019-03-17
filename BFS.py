#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# __author_: SHEN HONGCAI

from collections import deque

graph = {"A": ["B", "C"],
         "B": ["A", "C", "D"],
         "C": ["A", "B", "D", "E"],
         "D": ["B", "C", "E", "F"],
         "E": ["C", "D"],
         "F": ["D"]
        }


def bfs(graph, start):
    queue = deque()   # 用队列保存结点
    queue.append(start)
    seen = set()     # 用一个集合记录已经访问过的点
    seen.add(start)

    while queue:
        vertex = queue.popleft()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)


bfs(graph, "A")





