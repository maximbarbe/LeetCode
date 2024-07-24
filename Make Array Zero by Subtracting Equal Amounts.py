class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        substracted = 0
        res = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] - substracted > 0:
                substracted += (nums[i] - substracted)
                res += 1
        return res