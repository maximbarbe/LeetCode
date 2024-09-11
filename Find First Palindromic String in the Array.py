class Solution:

    def isPalindrome(self, w):
        start, end = 0, len(w) - 1
        while start < end:
            if w[start] != w[end]:
                return False
            start += 1
            end -= 1
        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""
