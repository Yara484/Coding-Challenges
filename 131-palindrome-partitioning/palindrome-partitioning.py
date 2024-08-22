class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []
        # i is start index and j is end index
        def backtrack(i):
            # Base Case
            if i == len(s):
                res.append(sol[:]) # Attach Copy
                return
            # Decision to choose
            for j in range(i, len(s)):
                # Check if string is a palindrome
                if self.isPalindrome(s, i, j):
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()

        backtrack(0)
        return res

    def isPalindrome(self, s, l ,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True        


