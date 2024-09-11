class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0 
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j].count("1") <= k or s[i:j].count('0') <= k:
                    res += 1
        return res