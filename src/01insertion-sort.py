import random

"""

・先頭の要素をソート済みとする
・未ソートの部分がなくなるまで、以下の処理を繰り返す。
    １．未ソート部分の先頭から要素を１つ取り出しｖに記録する
    ２．ソート済みの部分において、ｖより大きい要素を候補上１つづつ移動する。
    ３．最後に空いた位置に「取り出した要素ｖを挿入する。
"""


data = [random.randint(0, 100) for _ in range(10)]


# 鼠入ソート
for idx, number in enumerate(data):
    # 隣接する数値
    v = data[idx]
    j = idx - 1
    print(data)
    while j >= 0 and data[j] > v:
        data[j + 1] = data[j]
        j -= 1
        print(data)
    data[j + 1] = v  # ソート済み配列
    print(data)

print(data)
