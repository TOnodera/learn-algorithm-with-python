class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n
        self.size = [1] * n

    def root(self, x):
        if self.parent[x] == -1:
            return x

        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        self.size[rx] += self.size[ry]
        return True

    def size(self, x):
        return self.size[self.root(x)]
