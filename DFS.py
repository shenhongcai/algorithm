#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# __author_: SHEN Hongcai


def dfs(graph, start):
    stack = []   # 用队列保存结点
    stack.append(start)
    seen = set()     # 用一个集合记录已经访问过的点
    seen.add(start)

    while stack:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)


graph1 = {"A": ["B", "C"],
          "B": ["A", "C", "D"],
          "C": ["A", "B", "D", "E"],
          "D": ["B", "C", "E", "F"],
          "E": ["C", "D"],
          "F": ["D"]
        }


dfs(graph1, "A")