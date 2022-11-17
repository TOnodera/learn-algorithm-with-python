def gcd(m: int, n: int):
    # ベースケース
    if n == 0:
        return m
    return gcd(n, m % n)


print(gcd(51, 15))
