class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        diff = 0

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in mymap:
                mymap[nums[i]] = i
            else:
                return [mymap[diff], i] 