"""   
@Project Name: pycharmproj
@Author: Shen Hongcai
@Time: 2019-03-22, 15:57
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""

#import networkx as nx
#import random
import heapq
import timeit

# 用优先队列实现


def init_distance(graph,start):
    distance = {start: 0}
    for vertex in graph:
        if vertex is not start:
            distance[vertex] = float("inf")
    return distance


def dijkstra(graph,start):
    pqueue=[]
    heapq.heappush(pqueue, (start, 0))
    seen=set()
    parent = {start: None}
    distance = init_distance(graph, start)

    while pqueue:
        pairs = heapq.heappop(pqueue) # pick the minist vertex from pqueue
        u=pairs[0]
        dist=pairs[1]
        seen.add(u)

        nodes = graph[u].keys()  # 列出u的邻接点

        for w in nodes:
            if w not in seen:
                if dist+graph[u][w] < distance[w]:
                    heapq.heappush(pqueue, (w, dist + graph[u][w]))
                    parent[w] = u
                    distance[w] = dist+graph[u][w]

    return parent, distance






if __name__ == "__main__":

    M = 10000
    test_2 = [[0, 2, M, M, M, 6, M, M, M],
              [2, 0, 3, M, 1, M, M, M, M],
              [M, 3, 0, 1.5, M, M, M, M, M],
              [M, M, 1.5, 0, 1.4, M, M, M, 0.5],
              [M, 1, M, 1.4, 0, M, M, 10, M],
              [6, M, M, M, M, 0, 2, M, M],
              [M, M, M, M, M, 2, 0, 7, M],
              [M, M, M, M, 10, M, 7, 0, 3],
              [M, M, M, 0.5, M, M, M, 3, 0]
              ]
    row = len(test_2)
    col = len(test_2[0])
    graph2={}
    nodes = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I"}
    for i in range(row):
        graph2[nodes[i]]={}
        for j in range(col):
            if test_2[i][j]== M:
                pass
            else:
                graph2[nodes[i]][nodes[j]]=test_2[i][j]


    start="A"
    dijkstra(graph2, start)
    parent, distance = dijkstra(graph2,"A")

    end = "H"
    path = []
    while end:
        path.append(end)
        end = parent[end]
    print(path)


time1= timeit.Timer(stmt="dijkstra(graph2,start),start",setup="from __main__ import dijkstra,start,graph2")
print("使用优先队列的算法耗费时间为：%s s" % (time1.timeit(10)))











