class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = dict()
        maximum = -1
        for i in range(len(nums)):
            if seen.get(nums[i], False) == False:
                seen[-nums[i]] = True
            else:
                maximum = max(maximum, abs(nums[i]))
        return maximum