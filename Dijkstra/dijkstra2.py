import timeit
# !/usr/bin/python3.6
# -*- coding: utf-8 -*-
# __author_: 米兰小子


def dijkstra(graph, start, end):
    RG = graph.reverse()  # Reverse the original graph
    dist = {}  # Record the nearest distance from source node to the other nodes
    previous = {}  # store the parent node
    for v in RG.nodes():
        dist[v] = float("inf")  # Initialize the distance from source to the node to be routed
        previous[v] = "None"
    dist[end] = 0
    u = end
    alreadynode = set()
    notroutenode = {node for node in RG.nodes()}
    while u != start:
        u = min(dist, key=dist.get)  # Find the nearest distance node to be routed

        distu = dist[u]
        del dist[u]  # 将距离最短的顶点从待遍历结点里移除
        for u, v in RG.edges(u):
            if v in dist:
                alt = distu + RG[u][v]["weight"]  # 计算当前结点的代价 与 当前结点到其余结点的和
                if alt < dist[v]:
                    dist[v] = alt  # 更新v结点的距离代价
                    previous[v] = u  # 将前驱结点设置为u

        """ alreadynode.add(u)

        for i in notroutenode:
            for j in notroutenode:
                RG = self.update_map(i, j, RG)

        notroutenode.remove(u)
        """
    return previous, dist


"""
    path = [start, ]   # 用于保存从起始点出发所经过的路径结点
    last = start
    while last != end:
        nxt = previous[last]
        path.extend(nxt)
        last = nxt
    return path

"""


def route_from_src(graph, src):
    route = {src: {}}
    end = [node for node in graph.nodes()]
    for n in end:
        route[src][n] = dijkstra(graph, src, n)
    return route


def update_map(self, x, y, G):
    new_weight = random.uniform(10, 70)
    G.add_edge(x, y, weight=new_weight)
    return G


if __name__ == "__main__":

    M = 10000
    graph1 = nx.DiGraph()
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
    nodes = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I"}
    for i in range(row):
        for j in range(col):
            graph1.add_edge(nodes[i], nodes[j], weight=test_2[i][j])

    starting = "A"
    ending = "H"
    dijkstra(graph1, starting, ending)

# 测试性能
time1 = timeit.Timer(stmt="dijkstra(graph1,starting, ending),graph1,starting,ending", \
                     setup="from __main__ import dijkstra,graph1,starting,ending")
print("未使用优先队列算法运行时间：%s s" % (time1.timeit(10)))











