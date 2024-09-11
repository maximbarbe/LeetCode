class NeighborSum:

    def _getPos(self, grid):
        pos = dict()
        for i in range(len(grid)):
            for j in range(len(grid)):
                pos[grid[i][j]] = (i, j)

        return pos

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.pos = self._getPos(grid)
        self.n = len(grid)
    @lru_cache
    def adjacentSum(self, value: int) -> int:
        i, j = self.pos[value]
        res = 0
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if i + x >= 0 and i + x < self.n and j + y >= 0 and j + y < self.n:
                res += self.grid[i + x][y + j]
        return res

    @lru_cache
    def diagonalSum(self, value: int) -> int:
        i, j = self.pos[value]
        res = 0
        for x, y in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            if i + x >= 0 and i + x < self.n and j + y >= 0 and j + y < self.n:
                res += self.grid[i + x][y + j]
        return res


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)