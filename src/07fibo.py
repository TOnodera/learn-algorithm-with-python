class Fibo:
    def __init__(self):
        self.memo = []

    def fibo(self, N: int) -> int:

        if len(self.memo) == 0:
            self.memo = [-1 for _ in range(N + 1)]

        if N == 0:
            return 0
        elif N == 1:
            return 1
        if self.memo[N] != -1:
            return self.memo[N]

        self.memo[N] = self.fibo(N - 1) + self.fibo(N - 2)
        return self.memo[N]


f = Fibo()

print(f.fibo(100))
