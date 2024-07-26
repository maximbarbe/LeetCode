class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        converted = set()
        for word in words:
            c = ""
            for letter in word:
                c += alphabet[ord(letter) - ord('a')]
            converted.add(c)
        return len(converted)