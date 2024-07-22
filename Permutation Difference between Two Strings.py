class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        chars = dict()
        for i in range(len(s)):
            chars[s[i]] = i
        res = 0
        for i in range(len(t)):
            res += abs(i - chars[t[i]])
        return res