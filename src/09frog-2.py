INF = 1 << 60

N = 7
H = [2, 9, 4, 5, 1, 6, 10]

dp = [INF for _ in range(N + 1)]

i = 0
# 0番目に来るためのコストは０
dp[0] = 0
for i in range(0, N):
    if i + 1 < N:
        # 1番目に行くためのコスト
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(H[i + 1] - H[i]))
    if i + 2 < N:
        # i番目に行くためのコスト
        # 1つ先に行くか、2つ先に行くかのコストの小さいほうに向かう
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(H[i + 2] - H[i]))

print("Answer: ", dp[N - 1])
