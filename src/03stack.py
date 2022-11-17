import re


class Stack:
    def __init__(self, max: int) -> None:
        self.top = 0
        self.max = max
        self.data = []

    def isFull(self) -> bool:
        return self.top >= self.max

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def push(self, data: int) -> bool:
        if self.isFull():
            return False

        self.top += 1
        self.data.append(data)
        return True

    def pop(self) -> int:
        if self.isEmpty():
            return None
        return self.data.pop()


str = "5 40 * 10 1 + /"

stack = Stack(len(str))

for s in str.split(" "):

    if re.match(r"[+-/*]", s):
        v2 = stack.pop()
        v1 = stack.pop()
        if s == "+":
            stack.push(v1 + v2)
        if s == "-":
            stack.push(v1 - v2)
        if s == "*":
            stack.push(v1 * v2)
        if s == "/":
            stack.push(v1 / v2)
    else:
        stack.push(int(s))

print(stack.pop())
