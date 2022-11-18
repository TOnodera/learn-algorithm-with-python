INF = 1 << 60

N = 7
H = [2, 9, 4, 5, 1, 6, 10]

dp = [INF for _ in range(N + 1)]


def rec(i: int):
    if dp[i] < INF:
        return dp[i]

    if i == 0:
        return 0

    res = INF
    res = min(res, rec(i - 1) + abs(H[i] - H[i - 1]))

    if i > 1:
        res = min(res, rec(i - 2) + abs(H[i] - H[i - 2]))

    dp[i] = res
    return dp[i]


print(rec(N - 1))
