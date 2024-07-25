class Solution:


    def gen(self, left, right, cur, comb):
        if left == 0 and right == 0:
            comb.append(cur)
        elif left != 0 and right != 0:
            self.gen(left -1, right, cur + '(', comb)
            self.gen(left, right - 1, cur + ")", comb)
        elif left == 0:
            self.gen(left, right - 1, cur + ")", comb)
        else:
            self.gen(left -1, right, cur + '(', comb)

    def validate(self, par):
        stack = []
        for char in par:
            if stack == [] or char == "(":
                stack.append(char)
            else:
                if stack[-1] != "(":
                    return False
                stack.pop()
        return stack == []


    def generateParenthesis(self, n: int) -> List[str]:
        comb = []
        self.gen(n, n, "", comb)
        res = []
        for par in comb:
            if self.validate(par):
                res.append(par)
        return res