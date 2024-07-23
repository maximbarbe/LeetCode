class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        res = [None] * len(s)
        left, right = 0,len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                res[left], res[right] = s[left], s[left]
            else:
                m = min(s[left], s[right])
                res[left] = m
                res[right] = m
            left += 1
            right -= 1
        return "".join(res)