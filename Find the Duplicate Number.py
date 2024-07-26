class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if count[nums[i]] == 1:
                return nums[i]
            count[nums[i]] += 1