class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        return list(set(list(nums1.intersection(nums2)) + list(nums1.intersection(nums3)) + list(nums2.intersection(nums3))))