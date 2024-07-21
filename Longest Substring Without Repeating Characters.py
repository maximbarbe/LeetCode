class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()
        max_length = 0
        cur_length = 0
        start = 0
        for char in s:
            if c[char] == 0:
                cur_length += 1
                c[char] += 1
            else:
                while s[start] != char:
                    c[s[start]] -= 1
                    start += 1
                    cur_length -= 1

                start += 1

            if cur_length > max_length:
                max_length = cur_length
        return max_length