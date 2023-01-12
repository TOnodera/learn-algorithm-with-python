def bubble_sort(ARY, N):
    change_count = 0
    flag = True
    j = 0
    while flag:
        flag = False
        i = N - 1
        while i > j:
            if ARY[i] < ARY[i - 1]:
                ARY[i - 1], ARY[i] = ARY[i], ARY[i - 1]
                change_count += 1
                flag = True
            i -= 1
        j += 1

    return ARY


def selection_sort(ARY, N):
    change_count = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if ARY[j] < ARY[minj]:
                minj = j

        if minj != i:
            change_count += 1
            ARY[i], ARY[minj] = ARY[minj], ARY[i]

    return ARY


def is_stable(input, output):
    is_stable = True
    for idx, inp in enumerate(input):
        if not (
            input[idx][0:1] == output[idx][0:1] and input[idx][1:] == output[idx][1:]
        ):
            is_stable = False
    return is_stable
