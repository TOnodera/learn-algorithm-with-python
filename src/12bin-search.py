N = 8

A = [3, 5, 8, 10, 14, 17, 21, 39]


def bin_search(key: int):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] == key:
            return mid
        elif A[mid] > key:
            right = mid - 1
        elif A[mid] < key:
            left = mid + 1

    return -1


print(bin_search(10))
print(bin_search(3))
print(bin_search(39))
print(bin_search(-100))
print(bin_search(9))
print(bin_search(100))
