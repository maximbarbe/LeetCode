class Solution:
    def partitionString(self, s: str) -> int:
        seen = dict()
        res = 1
        for char in s:
            if seen.get(char, False) == False:
                seen[char] = True
            else:
                res += 1
                seen = dict()
                seen[char] = True
        return res