class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = defaultdict(lambda:0)
        for c in s:
            chars[c] += 1
        for key in chars.keys():
            if chars[key] == 1:
                return s.index(key)
        else:
            return -1