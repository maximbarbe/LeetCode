class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        innums1 = dict()
        innums2 = dict()
        for i in range(len(nums1)):
            innums1[nums1[i]] = True
        for i in range(len(nums2)):
            innums2[nums2[i]] = True
        r1 = []
        r2 = []
        for i in range(len(nums1)):
            if innums2.get(nums1[i], False) == False:
                r1.append(nums1[i])
        for i in range(len(nums2)):
            if innums1.get(nums2[i], False) == False:
                r2.append(nums2[i])
        return [r1, r2]