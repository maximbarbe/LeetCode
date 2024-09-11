class Solution:
    def countSegments(self, s: str) -> int:
        segments = 0
        cur = ""
        for char in s:
            if char != " ":
                cur += char
            else:
                if cur != '':
                    segments += 1
                cur = ''
        else:
            if cur != "":
                segments += 1
        return segments