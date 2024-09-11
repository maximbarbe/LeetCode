class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        cols = len(matrix)
        rows = len(matrix[0])
        res = []
        for i in range(rows):
            row = [0] * cols
            res.append(row)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res[j][i] = matrix[i][j]

        return res