class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for key in c.keys():
            if c[key] == 2:
                res ^= key
        return res