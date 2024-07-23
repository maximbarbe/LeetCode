class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        odd = False
        max_len = 0
        values = sorted(c.values(), reverse=True)
        for val in values:
            if val % 2 == 0:
                max_len += val
            else:
                if not odd:
                    max_len += val
                    odd = True
                else:
                    max_len += val - 1
        return max_len