class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        b1 = bin(start)[2:]
        b2 = bin(goal)[2:]
        if len(b1) < len(b2):
            b1 = b1.zfill(len(b1) + len(b2) - len(b1))
        if len(b2) < len(b1):
            b2 = b2.zfill(len(b2) + len(b1) - len(b2))
        res = 0
        for i in range(len(b1)):
            if b1[i] != b2[i]:
                res += 1
        return res