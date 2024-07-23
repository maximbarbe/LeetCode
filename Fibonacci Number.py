class Solution:
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n
        x1 = 0
        x2 = 1
        for i in range(2, n+1):
            cur = x2 + x1
            x1 = x2
            x2 = cur
        return x2