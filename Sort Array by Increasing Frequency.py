class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = dict()
        for i in range(len(nums)):
            if freq.get(nums[i], 0) == 0:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        nums.sort(key=lambda el:(freq[el], -el))
        return nums