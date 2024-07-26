class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if len(digits) == 0:
            return []
        cur= [""]
        for i in range(len(digits)):
            prev= cur
            cur = []
            for p in prev:
                for letter in dig[digits[i]]:
                    cur.append(p + letter)
        return cur 