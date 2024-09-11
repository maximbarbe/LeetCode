class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = [0] * len(A)
        for i in range(len(A)):
            res[i] = len(set(A[:i + 1]).intersection(set(B[:i+1])))
        return res