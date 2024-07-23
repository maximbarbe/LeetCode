class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            res = max(res, nums[left] + nums[right])
            left += 1
            right -= 1
        return res