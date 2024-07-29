class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        p = purchaseAmount
        if p % 10 <= 4:
            p -= p % 10
        else:
            p += 10 - p%10
        return 100 - p