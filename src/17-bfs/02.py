from queue import Queue

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

dist = [-1] * N

que = Queue()

dist[0] = 0

que.put(0)

while not que.empty():
    v = que.get()

    for next_v in G[v]:
        if dist[next_v] != -1:
            continue

        dist[next_v] = dist[v] + 1
        que.put(next_v)
