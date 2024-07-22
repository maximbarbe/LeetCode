class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda el:(bin(el).count('1'), el))
        return arr