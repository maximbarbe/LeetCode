class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = defaultdict(lambda:None)
        seen[(0, 0, 0, 0, 0)] = 0
        vowels = [0, 0, 0, 0, 0]
        max_length = 0
        for i in range(len(s)):
            match s[i]:
                case 'a':
                    vowels[0] ^= 1
                case 'e':
                    vowels[1] ^= 1
                case 'i':
                    vowels[2] ^= 1
                case 'o':
                    vowels[3] ^= 1
                case 'u':
                    vowels[4] ^= 1
            if seen[tuple(vowels)] == None:
                seen[tuple(vowels)] = i + 1
            else:
                max_length = max(max_length, i - seen[tuple(vowels)] + 1)
        return max_length