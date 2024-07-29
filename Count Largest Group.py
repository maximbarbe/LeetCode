class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(lambda:[])
        for i in range(1, n+1):
            temp = i
            digit_sum = 0
            while i != 0:
                digit_sum += i % 10
                i //= 10
            groups[digit_sum].append(temp)
        max_size = 0
        res = 0
        for val in groups.values():
            if len(val) > max_size:
                res = 1
                max_size = len(val)
            elif len(val) == max_size:
                res += 1
        return res