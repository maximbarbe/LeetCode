class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = defaultdict(lambda:[False, False])
        for char in s:
            if char.isupper():
                letters[char][0] = True
            else:
                letters[char.upper()][1] = True
        greatest_letter = None
        for key, val in letters.items():
            if val == [True, True]:
                if greatest_letter == None or key > greatest_letter:
                    greatest_letter = key
        return "" if greatest_letter == None else greatest_letter