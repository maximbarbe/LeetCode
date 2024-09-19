class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value = max(nums)
        max_length = 1
        cur_length = 0
        prev=  None
        for i in range(len(nums)):
            if nums[i] == prev:
                cur_length += 1
                if nums[i] == max_value and cur_length > max_length:
                    max_length = cur_length
            else:
                prev = nums[i]
                cur_length = 1
        return max_length