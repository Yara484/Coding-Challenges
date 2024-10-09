class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        myset = set(nums1)
        for num in nums2:
            if num in myset:
                res.append(num)
        return set(res)       