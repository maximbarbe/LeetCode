class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if nums[i] < k:
                res += 1
            else:
                break
        return res