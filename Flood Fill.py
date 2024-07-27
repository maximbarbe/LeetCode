class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src_color = image[sr][sc]
        q = deque([(sr, sc)])
        if image[sr][sc] == color:
            return image
        while len(q) != 0:
            i, j = q.popleft()
            image[i][j] = color
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if i + x >=0 and i + x < len(image) and y + j >= 0 and y + j < len(image[0]) and image[i + x][y + j ] == src_color:
                    q.append((i+x, y+j))
        return image