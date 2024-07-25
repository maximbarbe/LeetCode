class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        for i in range(0, len(nums), 2):
            nums[i] = evens.pop()
            nums[i + 1] = odds.pop()
        return nums