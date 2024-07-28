class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = [0] * 26
        for char in s:
            letters[ord(char) - ord('a')] += 1
            if letters[ord(char) - ord('a')] == 2:
                return char