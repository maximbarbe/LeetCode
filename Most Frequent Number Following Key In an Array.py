class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freq = Counter()
        for i in range(len(nums) - 1):
            if nums[i] == key:
                freq[nums[i + 1]] += 1
        max_freq = 0
        res = 0
        for key in freq:
            if freq[key] > max_freq:
                max_freq = freq[key]
                res = key
        return res