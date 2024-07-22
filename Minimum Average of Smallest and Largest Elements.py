class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        q = deque(sorted(nums))
        res = inf
        while len(q) != 0:
            x1 = q.popleft()
            x2 = q.pop()
            if (x1 + x2)/2 < res:
                res = (x1 + x2)/2
        return res