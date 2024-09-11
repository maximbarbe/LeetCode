class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        i, j = 0, -1
        res = []
        dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        idx = 0
        while len(res) != len(matrix) * len(matrix[0]):
            x, y = dirs[idx]
            if i + x >= 0 and i + x < len(matrix) and y + j >= 0 and y + j < len(matrix[0]) and (i + x, y+j) not in visited:
                res.append(matrix[i+x][y+j])
                visited.add((i+x, y+j))
                i += x
                j += y
            else:
                idx = (idx + 1)%4
        return res