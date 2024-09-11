class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted = "".join(map(str, [ord(char) - ord('a') + 1 for char in s]))
        dig_sum = 0
        for i in range(k):
            dig_sum = sum([int(char) for char in converted])
            converted = str(dig_sum)
        return dig_sum
