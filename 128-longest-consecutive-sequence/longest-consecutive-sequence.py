class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Using a hashset because it has O(1) lookup
        numSet = set(nums)
        res = 0

        for num in numSet:
            if (num - 1) not in numSet: # We have found start of sequence
                length = 1
                while (num + length) in numSet:
                    length += 1
                res = max(res, length)
        return res            
