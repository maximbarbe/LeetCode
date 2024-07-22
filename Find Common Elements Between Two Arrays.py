class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        intersect = set(nums1).intersection(nums2)
        res = [0, 0]
        for val in intersect:
            res[0] += c1[val]
            res[1] += c2[val]
        return res