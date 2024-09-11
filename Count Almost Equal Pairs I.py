class Solution:
    def countPairs(self, nums: List[int]) -> int:
        max_length = 0
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            if len(nums[i]) > max_length:
                max_length = len(nums[i])
        vals = list(map(lambda el:el.zfill(max_length), nums))
        res = 0
        for i in range(len(vals) -1):
            for j in range(i + 1, len(vals)):
                diff = 0
                for k in range(len(vals[i])):
                    if vals[i][k] != vals[j][k]:
                        diff += 1
                if diff in [0, 2] and Counter(vals[i]) == Counter(vals[j]):
                    res += 1
        return res