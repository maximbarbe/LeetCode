class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        res = -1
        for key in c.keys():
            if c[key] == key:
                res = max(res, key)
        return res