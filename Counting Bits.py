class Solution:

    def count(self, n):
        res = 0
        while n != 0:
            if n % 2 == 1:
                res += 1
            n //= 2
        return res
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.count(i))
        return res