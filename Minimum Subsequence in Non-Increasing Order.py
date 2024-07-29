class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        not_included = sum(nums)
        res = []
        included = 0
        for i in range(len(nums)):
            res.append(nums[i])
            included += nums[i]
            not_included -= nums[i]
            if included > not_included:
                return res