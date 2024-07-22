class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for  char in stones:
            if char in jewels:
                res += 1
        return res