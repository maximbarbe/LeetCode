class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = s.count(letter)
        if c == 0:
            return 0
        return floor((c/len(s))*100)