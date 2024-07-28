class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        chars = defaultdict(lambda:[])
        for i in range(len(s)):
            chars[s[i]].append(i)
        res = -1
        for key in chars.keys():
            if len(chars[key]) > 1:
                res = max(res, chars[key][-1] - chars[key][0] - 1)
        return res