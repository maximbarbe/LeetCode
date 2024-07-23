class MinStack:

    def __init__(self):
        self.stack = []
        self.min_el = inf
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_el:
            self.min_el = val

    def pop(self) -> None:
        if self.stack[-1] == self.min_el:
            self.stack.pop()
            if self.stack == []:
                self.min_el = inf
            else:
                self.min_el= min(self.stack)
        else:
            self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_el


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()