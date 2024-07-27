class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        in_arr = dict()
        for num in arr:
            in_arr[num] = True
        cur = 0
        while k != 0:
            cur += 1
            if in_arr.get(cur, False) == False:
                k -= 1
        return cur