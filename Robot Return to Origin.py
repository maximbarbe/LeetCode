class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for char in moves:
            match char:
                case "U":
                    y += 1
                case "D":
                    y -= 1
                case "L":
                    x -= 1
                case _:
                    x += 1
        return x == 0 and y == 0