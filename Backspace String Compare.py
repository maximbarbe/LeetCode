class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        for char in s:
            if char == "#":
                if s1 != []:
                    s1.pop()
            else:
                s1.append(char)
        s2 = []
        for char in t:
            if char == "#":
                if s2 != []:
                    s2.pop()
            else:
                s2.append(char)
        return s1 == s2