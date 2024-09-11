class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        first = s[:len(s)//2]
        sec = s[len(s)//2:]
        c1 = 0
        c2 = 0
        for char in first:
            if char in vowels:
                c1 += 1
        for char in sec:
            if char in vowels:
                c2 += 1
        return c1 == c2