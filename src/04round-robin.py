from typing import List


class PP:
    name = ""
    t = 0


p = [PP() for _ in range(1000)]

for l in p:
    print(l.name)
