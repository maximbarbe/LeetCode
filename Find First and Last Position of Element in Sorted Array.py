class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = bisect_left(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        else:
            return [first, bisect_right(nums, target) - 1]