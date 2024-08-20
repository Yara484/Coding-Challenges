class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        # Sorting Array
        nums.sort()
        
        def backtrack(i):
            # Base Case
            if i == len(nums):
                res.append(sol[:]) # Attach Copy
                return

            # Decision to choose
            sol.append(nums[i])
            backtrack(i+1)

            # Decision to skip
            sol.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)

        backtrack(0)
        return res            