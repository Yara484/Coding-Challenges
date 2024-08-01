class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Using hashset
        myset = set()
        for i in nums:
            if i in myset:
                return True
            else:
                myset.add(i)
        return False            