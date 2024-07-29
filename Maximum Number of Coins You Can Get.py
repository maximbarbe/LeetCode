class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        first, sec, end = 0, 1, len(piles) - 1
        res = 0
        while sec < end:
            res += piles[sec]
            first = sec + 1
            sec = first + 1
            end -= 1
        return res