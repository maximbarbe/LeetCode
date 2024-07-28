class Solution:
    def minimumSum(self, num: int) -> int:
        new1, new2 = [], []
        num = [char for char in str(num)]
        num.sort()
        new1.append(num[0])
        new1.append(num[2])
        new2.append(num[1])
        new2.append(num[3])
        return int("".join(new1)) + int("".join(new2))
        