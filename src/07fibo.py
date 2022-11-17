def fibo(N: int) -> int:
    print("再起関数を呼び出しました: ", N)
    if N == 0:
        return 0
    elif N == 1:
        return 1

    result = fibo(N - 1) + fibo(N - 2)
    print(N)
    return result


print(fibo(4))
