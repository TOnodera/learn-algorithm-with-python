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


def dfs(G, t):
    for next_v in G[t[0]][t[1]]:
        i, j = next_v
        if dist[i][j] != -1:
            continue
        dist[i][j] = dist[v] + 1
        dfs(G, (i, j))


INPUT = input()
a, b = INPUT.split()
H, W = int(a), int(b)

matrix = []
S = (0, 0)
for i in range(H):
    for m in input().split():
        matrix.append(list(m))

for i, m in enumerate(matrix):
    for j, r in enumerate(m):
        if matrix[i][j] == "S":
            S = (i, j)

G = [[[] for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if matrix[i][j] == "#":
            continue
        # 上
        if i - 1 >= 0 and (matrix[i - 1][j] != "#"):
            G[i][j].append((i - 1, j))
            G[i - 1][j].append((i, j))
        # 下
        if i + 1 < H and (matrix[i + 1][j] != "#"):
            G[i][j].append((i + 1, j))
            G[i + 1][j].append((i, j))
        # 左
        if j - 1 >= 0 and (matrix[i][j - 1] != "#"):
            G[i][j].append((i, j - 1))
            G[i][j - 1].append((i, j))
        # 右
        if j + 1 < W and (matrix[i][j + 1] != "#"):
            G[i][j].append((i, j + 1))
            G[i][j + 1].append((i, j))

dist = [[-1 for _ in range(W)] for _ in range(H)]
print(dist)
