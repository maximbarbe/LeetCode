class Solution:
    def clearDigits(self, s: str) -> str:
        kept = [True] * len(s)
        for i in range(len(s)):
            if s[i].isnumeric():
                kept[i] = False
                for j in range(i -1, -1, -1):
                    if not s[j].isnumeric() and kept[j]:
                        kept[j] = False
                        break
        res = ""
        for i in range(len(s)):
            if kept[i]:
                res += s[i]
        return res