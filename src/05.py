import random

"""
ビットを用いる部分和の実装
"""
exist = False
W = 101
N = 10
A = [random.randint(1, 10) for _ in range(1 << N)]
bit = 0

while bit < (1 << N):
    bit += 1
    sum = 0
    i = 0
    while i < N:
        i += 1
        if bit & (1 << i):
            sum += A[i]

    if sum == W:
        exist = True

if exist:
    print("True")

print(W)
