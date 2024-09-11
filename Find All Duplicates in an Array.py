class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numbers = [0] * (10**5 + 1)
        for v in nums:
            numbers[v] += 1
        return [i for i in range(len(numbers)) if numbers[i] > 1]