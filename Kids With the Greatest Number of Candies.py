class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        res = [False] *(len(candies))
        for i, c in enumerate(candies):
            if c + extraCandies >= maximum:
                res[i] = True
        return res