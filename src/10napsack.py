H = [(2, 3), (1, 2), (3, 6), (2, 1), (1, 3), (5, 85)]

N = len(H)

W = 14

dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]


for i, h in enumerate(H):
    for w in range(W + 1):
        if w > W:
            break

        if w - H[i][0] >= 0:
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - H[i][0]] + H[i][1])

        dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])
print(dp[N][W])
