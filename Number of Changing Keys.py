class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        res = 0
        prev = s[0]
        for i in range(1, len(s)):
            if s[i] != prev:
                res += 1
                prev = s[i]
        return res