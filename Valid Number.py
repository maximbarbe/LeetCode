class Solution:
    def isNumber(self, s: str) -> bool:
        if "inf" in s.lower() or s == "nan":
            return False
        try:
            float(s)
            return True
        except:
            return False