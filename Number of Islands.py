class Solution:

    def bfs(self, i, j, grid, visited):
        visited[i][j] = True
        q = deque([(i, j)])
        while len(q) != 0:
            x, y = q.popleft()
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if x + i >= 0 and x + i < len(grid) and y + j >= 0 and y + j < len(grid[0]) and grid[x+i][y+j] == '1' and visited[x+i][y+j] == False:
                    visited[x + i][y + j] = True
                    q.append((x + i, y +j))
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] == False:
                    res += 1
                    self.bfs(i, j, grid, visited)
        return res