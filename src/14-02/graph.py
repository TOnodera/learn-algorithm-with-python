class Edge:
    def __init__(self, to: int, weight: int):
        self.to = to
        self.weight = weight


NM = input()
N, M = NM.split(" ")

G = []
for i in range(int(M)):
    a, b, w = input().split(" ")
    G.append((a, Edge(b, w)))

print(G)
