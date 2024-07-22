class Solution:

    def shift(self, char, digit):
        return chr(ord(char) + digit)

    def replaceDigits(self, s: str) -> str:
        res = [char for char in s]
        for i, char in enumerate(res):
            if char.isdigit():
                res[i] = self.shift(res[i - 1], int(char))
        return "".join(res)