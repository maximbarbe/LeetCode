class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {tuple(obstacles[i]):True for i in range(len(obstacles))}
        cur = [0, 0]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        max_dist = 0
        cur_dir = 0
        for c in commands:
            match c:
                case -1:
                    cur_dir = (cur_dir + 1)%4
                case -2:
                    cur_dir = (cur_dir - 1)%4
                case _:
                    x, y = dirs[cur_dir]
                    for i in range(c):
                        if obstacles.get((cur[0] + x, cur[1] + y), False) == False:
                            cur[0] += x
                            cur[1] += y
                        if cur[0] ** 2 + cur[1]**2 > max_dist:
                            max_dist = cur[0] ** 2 + cur[1]**2

        return max_dist