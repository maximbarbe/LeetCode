class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumn = sum(nums[:k])
        max_average = sumn/k
        for i in range(k, len(nums)):
            sumn -= nums[i - k]
            sumn += nums[i]
            if sumn/k > max_average:
                max_average = sumn/k
        return max_average
        