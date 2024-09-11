class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return gcd(*set(Counter(deck).values())) > 1
    
