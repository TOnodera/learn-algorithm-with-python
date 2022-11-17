from typing import List


def partial_sum(i: int, w: int, A: List[int]):
    if i == 0:
        return w == 0

    # a[i-1]を選ばない場合
    if partial_sum(i - 1, w, A):
        return True

    # a[i-1]を選ぶ場合
    if partial_sum(i - 1, w - A[i - 1], A):
        return True

    return False


N = 4
W = 14
A = [3, 2, 6, 5]

if partial_sum(N, W, A):
    print("YES")
else:
    print("NO")
