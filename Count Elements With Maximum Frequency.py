class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c= Counter(nums)
        max_freq = 0
        count = 0
        for el in c.keys():
            if c[el] > max_freq:
                max_freq = c[el]
                count = 1
            elif c[el] == max_freq:
                count += 1
        return max_freq * count