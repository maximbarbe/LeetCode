class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = 0
        max_diag = 0
        for l, w in dimensions:
            diag = sqrt(l**2 + w**2)
            if diag > max_diag:
                area = l*w
                max_diag = diag
            elif diag == max_diag:
                if l*w > area:
                    area = l*w

        return area