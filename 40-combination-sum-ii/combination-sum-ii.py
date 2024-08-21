class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        candidates.sort()

        def backtrack(i, total):
            # Base Cases
            if total == target:
                res.append(sol[:])
                return
            if i == len(candidates) or total > target:
                return

            # Decision to choose
            sol.append(candidates[i])
            backtrack(i+1, total + candidates[i])

            # Decision not to choose
            sol.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, total)        

        backtrack(0 , 0)
        return res    