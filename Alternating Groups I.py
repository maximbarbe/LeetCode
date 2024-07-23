class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res = 0
        for i in range(len(colors)):
            if colors[i] == colors[(i + 2)%len(colors)] and colors[i] != colors[(i + 1)%len(colors)]:
                res += 1
        return res