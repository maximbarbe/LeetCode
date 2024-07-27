class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        down = True
        grid = [[None for i in range(len(s))] for j in range(numRows)]
        idx = 0
        i,j = 0,0
        while idx != len(s):
            if down:
                grid[i][j] = s[idx]
                i += 1
            else:
                grid[i][j] = s[idx]
                i -= 1
                j += 1
            if i == numRows - 1:
                down = False
            elif i == 0:
                down = True
            idx += 1
        res = ""
        for i in range(numRows):
            for j in range(len(s)):
                if grid[i][j] != None:
                    res += grid[i][j]
        return res