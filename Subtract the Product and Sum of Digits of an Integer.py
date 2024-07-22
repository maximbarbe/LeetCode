class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        while n != 0:
            dig = n%10
            prod *= dig
            sum += dig
            n //= 10
        return prod - sum
