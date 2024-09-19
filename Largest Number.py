class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        for i in range(len(nums) - 1):
            for j in range(i +1, len(nums)):
                if int(nums[i] + nums[j]) >= int(nums[j] + nums[i]):
                    continue
                else:
                    nums[j], nums[i] = nums[i], nums[j]
        return str(int(''.join(nums)))