class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = dict()
        cols = dict()
        for i in range(len(matrix)):
            rows[i] = min(matrix[i])
        for j in range(len(matrix[0])):
            cols[j] = max(matrix[i][j] for i in range(len(matrix)))
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == rows[i] and matrix[i][j] == cols[j]:
                    res.append(matrix[i][j])
        return res