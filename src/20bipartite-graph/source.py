import sys

sys.setrecursionlimit(1000000)

MAX_V = 1000

V = int(input())
E = int(input())
G = [[] for _ in range(MAX_V)]

for i in range(E):
    s, t = map(int, input().split())
    G[s].append(t)
    G[t].append(s)

color = [0] * MAX_V


def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False


for i in range(V):
    if color[i] == 0:
        if not dfs(i, 1):
            print("No")
            sys.exit()

print("Yes")
