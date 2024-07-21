class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, val in enumerate(nums):
            if seen.get(val, None) != None:
                return [seen[val], i]
            else:
                seen[target-val] = i