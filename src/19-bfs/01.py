from queue import Queue

# BFS
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

dist = [-1] * N

queue = Queue()

dist[0] = 0

queue.put(0)

# スタックに次に探索するべき頂点が入っているので
# 探索する頂点がなくなるまでループする
while not queue.empty():
    v = queue.get()
    # その頂点からいける（たどれる）頂点を一個ずつ調べる
    for next_v in G[v]:
        if dist[next_v] != -1:
            continue

        # その頂点に何手目で到達できるか記録する
        dist[next_v] = dist[v] + 1
        # 次に探索する頂点を入れておく
        queue.put(next_v)

print(dist)
