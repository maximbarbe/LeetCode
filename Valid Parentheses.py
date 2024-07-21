class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if stack == [] or char in "({[":
                stack.append(char)
            else:
                if char == ")":
                    if stack.pop() != "(":
                        return False
                elif char == "}":
                    if stack.pop() != "{":
                        return False
                else:
                    if stack.pop() != "[":
                        return False
        if stack == []:
            return True
        else:
            return False