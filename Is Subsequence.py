class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0

        for i in range(len(t)):
            if s_idx == len(s):
                return True
            if t[i] == s[s_idx]:
                s_idx += 1
        else:
            if s_idx == len(s):
                return True
            else:
                return False