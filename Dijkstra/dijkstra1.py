#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# __author_: SHEN HONGCAI

import heapq
import math


graph = {"A": {"B": 5, "C": 1},
         "B": {"A": 5, "C": 2, "D": 1},
         "C": {"A": 1, "B": 2, "D": 4, "E": 8},
         "D": {"B": 1, "C": 4, "E": 3, "F": 6},
         "E": {"C": 8, "D": 3},
         "F": {"D": 6}
        }




def init_distance(graph, s):

    distance = {s: 0}
    for vertex in graph:
        if vertex is not s:
            distance[vertex] = math.inf
    return distance


def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s: None}
    distance = init_distance(graph, s)

    while pqueue:
        pair = heapq.heappop(pqueue)    # 从优先队列中取出最小点
        dist = pair[0]
        vertext = pair[1]
        seen.add(vertext)

        nodes = graph[vertext].keys()    # 列出vertext的邻接点
        for w in nodes:
            if w not in seen:
                if dist + graph[vertext][w] < distance[w]:
                    heapq.heappush(pqueue, (dist+graph[vertext][w], w))
                    parent[w] = vertext
                    distance[w] = dist + graph[vertext][w]
    return parent, distance


parent, distance = dijkstra(graph, "B")
end = "A"
path=[]
while end:
    path.append(end)
    end = parent[end]

path.reverse
print(path)









