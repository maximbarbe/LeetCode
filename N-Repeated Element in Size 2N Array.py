class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        c = Counter(nums)
        for key in c.keys():
            if c[key] == len(nums)/2:
                return key