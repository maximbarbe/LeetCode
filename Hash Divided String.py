class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = []
        for i in range(0,len(s), k):
            res.append(chr(ord('a') + (sum([ord(char) for char in s[i:i+k]]) - k*ord('a'))%26))
        return "".join(res)