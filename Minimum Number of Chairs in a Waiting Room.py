class Solution:
    def minimumChairs(self, s: str) -> int:
        cur = 0
        maximum = 0
        for i in range(len(s)):
            match s[i]:
                case "E":
                    cur += 1
                case "L":
                    cur -= 1
            maximum = max(cur, maximum)
        return maximum