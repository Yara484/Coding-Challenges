class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        charmap = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        res, sol = [], []
        def backtrack(i):
            # Base Case
            if i == len(digits):
                res.append(''.join(sol))   
                return
            # Decision
            for letter in charmap[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return res            