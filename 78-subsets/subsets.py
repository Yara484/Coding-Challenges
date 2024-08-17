class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i):
            # Base Case
            if i == len(nums):
                res.append(sol[:]) # Storing copy of sol
                return
            # Yes Decision
            sol.append(nums[i])
            backtrack(i+1) # Explore Decision

            # No Decision
            sol.pop()
            backtrack(i+1) # Backtrack to start over

        backtrack(0)
        return res        