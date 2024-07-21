class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        threshold = floor(len(nums)/3)
        for key in c.keys():
            if c[key] > threshold:
                res.append(key)
        return res