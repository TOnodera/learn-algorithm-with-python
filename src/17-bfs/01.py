import sys

input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
g = [[] for _ in range(n)]


for _ in range(m):
    a, b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)


# -1 はまだ探索されていない頂点
dist = [-1] * n

nodes = [[] for i in range(n)]

# 頂点0を始点とする
dist[0] = 0
# 最初の頂点集合
nodes[0] = [0]

print("before nodes", nodes)
print("before dist", dist)
print("before g", g)

# k手目の探索する
for k in range(1, n):
    for v in nodes[k - 1]:
        for next_v in g[v]:
            if dist[next_v] != -1:
                continue

            dist[next_v] = dist[v] + 1
            nodes[k].append(next_v)

print("after nodes", nodes)
print("after dist", dist)
print("after g", g)
