class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            if len(str(i)) % 2 == 0:
                digits = [char for char in str(i)]
                if sum(map(int, digits[:len(digits)//2])) == sum(map(int, digits[len(digits)//2:])):
                    res += 1
        return res