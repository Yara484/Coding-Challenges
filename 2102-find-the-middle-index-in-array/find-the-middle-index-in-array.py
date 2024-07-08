class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre = []
        post = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                pre.append(0)
            else:
                pre.append(nums[i-1] + pre[i-1]) 

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                post[i] = 0
            else:
                post[i] = nums[i+1] + post[i+1]    

        for i in range(len(pre)):
            a = pre[i]
            b = post[i]
            if a == b:
                return i
        return -1        