class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myset = set(nums1)  # Create a set from the first array for O(1) lookups
        res = set()         # Use a set to store the intersection for uniqueness
        for num in nums2:
            if num in myset:
                res.add(num)  # Add to the result set if it's in the first set

        return res        


              

       