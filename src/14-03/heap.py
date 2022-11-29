class Heap:
    def __init__(self) -> None:
        self.heap = []

    def push(self, x) -> None:
        self.heap.append(x)
        i = len(self.heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.heap[p] >= x:
                break

            self.heap[i] = self.heap[p]
            i = p
        self.heap[i] = x

    def top(self) -> int:
        if len(self.heap) != 0:
            return self.heap[0]
        return -1

    def pop(self):
        if len(self.heap) == 0:
            return
        x = self.heap.pop()  # スタックのpop
        i = 0
        while i * 2 + 1 < len(self.heap):
            child_left = i * 2 + 1
            child_right = i * 2 + 2
            if (
                child_right < len(self.heap)
                and self.heap[child_left] < self.heap[child_right]
            ):
                child_left = child_right

            if self.heap[child_left] <= x:
                break

            self.heap[i] = self.heap[child_left]
            i = child_left

        self.heap[i] = x


h = Heap()
h.push(5)
h.push(3)
h.push(7)
h.push(1)
assert h.top() == 7
h.pop()
assert h.top() == 5
h.push(11)
assert h.top() == 11
