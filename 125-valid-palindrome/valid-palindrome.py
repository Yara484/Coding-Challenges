class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for c in range(len(s) - 1, -1, -1):
            if s[c].isalnum():
                res.append(s[c])
        
        s = ''.join([char for char in s if char.isalnum()])
        res = "".join(res)    
        return res.lower() == s.lower()  