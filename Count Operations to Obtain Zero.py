class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0
        while num1 != 0 and num2!=0:
            operations += 1
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
        return operations
        