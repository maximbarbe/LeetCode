class Solution:
    
    def bfs(self, i, j, grid, visited):
        q = deque([(i, j)])
        visited[i][j] = True
        res = 0
        while len(q) != 0:
            i, j = q.popleft()
            res += 1
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if i + x >= 0 and i + x < len(grid) and y + j >= 0 and y + j < len(grid[0]) and grid[i + x][y +j] == 1 and visited[i + x][y + j] == False:
                    q.append((i + x, y + j))
                    visited[i + x][y + j] = True
        return res

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum = 0
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == False:
                    maximum = max(maximum, self.bfs(i, j, grid, visited))
        return maximum