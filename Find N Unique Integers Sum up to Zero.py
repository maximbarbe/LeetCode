class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 1:
            res = [0]
            n -= 1
            for i in range(1, n//2 + 1):
                res.append(i)
                res.append(-i)
            return res
        else:
            res = []
            for i in range(1, n//2 + 1):
                res.append(i)
                res.append(-i)
            return res