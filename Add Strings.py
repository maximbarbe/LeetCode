class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        idx = 0
        res = ""
        while idx < len(num1) and idx < len(num2):
            add = int(num1[idx]) + int(num2[idx]) + carry
            carry = add// 10
            add %= 10
            res += str(add)
            idx += 1
        while idx < len(num1):
            add = int(num1[idx]) + carry
            carry = add// 10
            add %= 10
            res += str(add)
            idx += 1
        while idx < len(num2):
            add = int(num2[idx]) + carry
            carry = add// 10
            add %= 10
            res += str(add)
            idx += 1
        if carry == 1:
            res += str(1)
        return res[::-1]