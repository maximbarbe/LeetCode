class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        digits = []
        for num in nums:
            cur = []
            while num != 0:
                cur.append(num%10)
                num //= 10
            for i in range(len(cur) - 1, -1, -1):
                digits.append(cur[i])
        return digits