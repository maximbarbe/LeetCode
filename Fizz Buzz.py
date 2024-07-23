class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            add = ""
            if i % 3 == 0:
                add += "Fizz"
                if i % 5 == 0:
                    add += "Buzz"
            elif i% 5 == 0:
                add += "Buzz"
            else:
                add += str(i)
            res.append(add)
        return res