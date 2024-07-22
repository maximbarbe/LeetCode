class Solution:
    def balancedStringSplit(self, s: str) -> int:
        right = 0
        left = 0
        res = 0
        for char in s:
            if char == "R":
                right += 1
            else:
                left += 1
            if left == right:
                res += 1
                right = 0
                left = 0
        return res