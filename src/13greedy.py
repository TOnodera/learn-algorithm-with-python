import math

V = [500, 100, 50, 10, 5, 1]


A = [1, 10, 3, 4, 5, 6]


X = 999

result = 0
for i in range(len(V)):
    add = X // V[i]
    if add > A[i]:
        add = A[i]

    X = X - (V[i] * add)
    result = result + add
    print(V[i], f"円は{add}枚")

print(result)
