class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i, total):
            # Base Cases
            if total == target:
                res.append(sol[:]) # Append a copy
                return
            if i == len(candidates) or total > target:
                return

            # Decision to choose
            sol.append(candidates[i])
            backtrack(i, total+candidates[i])

            # Decision not to choose
            sol.pop()
            backtrack(i+1, total)

        backtrack(0, 0) 
        return res   
