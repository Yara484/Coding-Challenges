class Solution:
    def isPalindrome(self, s: str) -> bool:
        word1 = ''
        word2 = ''
        s = s.lower()

        for char in s:
            if char.isalnum():
                word1 += char


        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                word2 += s[i]

        return word1 == word2                