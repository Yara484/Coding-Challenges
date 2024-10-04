class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in myMap:
                return [myMap[val], i]
            else:
                myMap[nums[i]] = i
""""
nums = [2,7,11,15], target = 9
i = 0
val = 9 - 2 = 7, 
{
    2 : 0
}


"""