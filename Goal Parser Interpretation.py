class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        res = ""
        for char in command:
            if char == "G":
                res += "G"
            else:
                if char in "(al":
                    stack.append(char)
                else:
                    if stack[-1] == "(":
                        stack.pop()
                        res += "o"
                    else:
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        res += "al"
        return res