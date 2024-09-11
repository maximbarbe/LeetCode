class Solution:
    def sortVowels(self, s: str) -> str:
        chars = [char for char in s]
        vowels = "aeiouAEIOU"
        v = []
        for i, char in enumerate(chars):
            if char in vowels:
                v.append(char)
                chars[i] = "_"
        v.sort(key=ord)
        idx = 0
        for i in range(len(chars)):
            if chars[i] == "_":
                chars[i] = v[idx]
                idx += 1
        return "".join(chars)