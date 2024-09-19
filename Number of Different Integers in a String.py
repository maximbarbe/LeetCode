class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        integers = set()
        cur = ''
        for char in word:
            if char.isdigit():
                cur += char
            else:
                if cur != '':
                    integers.add(int(cur))
                    cur = ""
        else:
            if cur != '':
                integers.add(int(cur))
                cur = ""
        return len(integers)