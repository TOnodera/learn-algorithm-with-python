def dfs(G, v):
    for next_v in G[v]:
        if dist[next_v] != -1:
            continue
        dist[next_v] = dist[v] + 1
        print("行きがけ: ", v)
        dfs(G, next_v)
        print("帰りがけ: ", v)


# DFS
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

dist = [-1] * N
dist[0] = 0

dfs(G, 0)

print(dist)
