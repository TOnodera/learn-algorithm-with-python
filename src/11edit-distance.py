INF = 1 << 29


S = "logistic"
T = "algorithm"

dp = [[INF for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]

dp[0][0] = 0

for i in range(len(S) + 1):
    for j in range(len(T) + 1):
        # 変更
        if i > 0 and j > 0:
            if S[i - 1] == T[i - i]:
                dp[i][j] = min(dp[i][j], dp[i][j] + 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        # 削除
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
        # 挿入
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

print(dp[len(S)][len(T)])
