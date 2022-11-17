import random

data = [random.randint(0, 100) for _ in range(10)]

"""
配列の末尾から隣接する要素を順番に比べていき、大小関係が逆ならば交換する
"""


def bubble_sort(data):
    """バブルソート：前から2つずつデータを比較し並べ替える．ただし，交換がもう必要ない所は省略する"""
    change = True  # 交換の余地ありと仮定

    for i in range(len(data)):
        if not change:  # 交換の余地無しで繰り返し脱出
            break
        change = False  # 交換の余地無しと仮定
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:  # 左の方が大きい場合
                data[j], data[j + 1] = data[j + 1], data[j]  # 前後入れ替え
                change = True  # 交換の余地ありかも

    return data


print(data)
bubble_sort(data)
print(data)
