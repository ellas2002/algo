from src.practice.FloydWarshall import *

def shortest_paths(graph):
    v = len(graph.edge)
    d = [[float('inf') for _ in range(v)] for _ in range(v)] #create a 2d array
    for i in range(v):
        d[i][i] = 0
        for j, weight in graph.adj[i]:
            d[i][j] = weight[i][j]
    for k in range(v):
        for i in range(v):
            for w in range(v):
                if d[k][i] + d[i][w] < d[i][w]:
                    d[x][w] = d[k][i]

    return d


g = FloydWarshall(7)
g.add_edge(0,1,4)
g.add_edge(0,2,5)
g.add_edge(1,2,6)
g.add_edge(2,3,7)
g.add_edge(3,5,1)
g.add_edge(5,6,2)
g.add_edge(0,4,2)

#print(shortest_paths(g))
d = shortest_paths(g)

for row in d:
    print(row)
