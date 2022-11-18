INF = 1 << 60

N = 7
H = [2, 9, 4, 5, 1, 6, 10]

dp = [INF for _ in range(N + 1)]

i = 0
# 0番目に来るためのコストは０
dp[0] = 0
for i in range(1, N):
    if i == 1:
        # 1番目に来るためのコスト
        dp[i] = abs(H[i] - H[i - 1])
    else:
        # i番目に来るためのコストは1つ前から来るか、2個前から来る場合のうち小さいほう
        dp[i] = min(dp[i - 1] + abs(H[i] - H[i - 1]), dp[i - 2] + abs(H[i] - H[i - 2]))

print("Answer: ", dp[N - 1])
