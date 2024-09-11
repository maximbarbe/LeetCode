class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        res = 0
        for char in "abcdefghijlmnopqrstuvwxyz":
            if char in word and char.upper() in word:
                res += 1
        return res