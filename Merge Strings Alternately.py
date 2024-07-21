class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += word1[i]
            res += word2[i]
        res += word1[i + 1:]
        res += word2[i + 1:]
        return res