class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(len(nums1)):
            idx = bisect_left(nums2, nums1[i])
            if idx < len(nums2) and nums2[idx] == nums1[i]:
                return nums1[i]
        return -1