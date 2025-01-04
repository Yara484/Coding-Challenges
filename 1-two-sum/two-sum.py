class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in mymap:
                mymap[nums[i]] = i
            else:
                return [i,mymap[diff]]
        