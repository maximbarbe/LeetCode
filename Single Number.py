class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        els = [0] * (60001)
        for i in range(len(nums)):
            els[nums[i] + 30000] += 1
        for i in range(len(els)):
            if els[i] == 1:
                return i - 30000