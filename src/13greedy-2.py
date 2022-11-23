class Intereval:
    def __init__(self, first: int, second: int):
        self.first = first
        self.second = second


data = [Intereval(1, 2), Intereval(2, 5), Intereval(3, 4), Intereval(5, 10)]

res = 0
current_end_time = 0

for i in range(len(data)):
    if data[i].first < current_end_time:
        continue

    res += 1
    current_end_time = data[i].second

print(res)
