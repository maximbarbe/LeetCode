class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        for i in range(len(nums) -2):
            for j in range(i + 1, len(nums) - 1):
                if nums[j] - nums[i] > diff:
                    break
                elif nums[j] - nums[i] == diff:
                    for k in range(j + 1, len(nums)):
                        if nums[k] - nums[j] > diff:
                            break
                        elif nums[k] - nums[j] == diff:
                            res += 1
        return res