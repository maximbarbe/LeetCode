class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        max_length = 0
        if len(a) != len(b):
            return max(len(a), len(b))
        for i in range(len(a)):
            for j in range(i + 1, len(a) + 1):
                if j - i > max_length and a[i:j] not in b:
                    max_length = j - i
        return max_length if max_length != 0 else -1