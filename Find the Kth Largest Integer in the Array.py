class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(lambda el: -int(el), nums))
        heapq.heapify(nums)
        cur = None
        for i in range(k):
            cur = heapq.heappop(nums)
        return str(-cur)