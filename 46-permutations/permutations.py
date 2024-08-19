class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: n!
        res, sol = [], []
        def backtrack():
            # Base Case
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            # Decision To Choose
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()

        backtrack()
        return res                