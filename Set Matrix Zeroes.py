class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for r in rows:
            for j in range(len(matrix[r])):
                matrix[r][j] = 0
        for i in range(len(matrix)):
            for c in cols:
                matrix[i][c] = 0