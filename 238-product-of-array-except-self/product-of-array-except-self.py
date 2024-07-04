class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = [1 for i in range(len(nums))]
        res = []

        for i in range(len(nums)):
            if i == 0:
                pre.append(1)
            else:
                pre.append(nums[i-1] * pre[i-1])   

        for i in range(len(nums)-1, -1, -1):
            if i == (len(nums)-1):
                continue
            else:
                post[i] = nums[i+1] * post[i+1]

        for i in range(len(pre)):
            res.append(pre[i] * post[i])

        return res    


'''
nums = [1,2,3,4]
prefix = [1, 1, 2, 6]
postfix = [24, 12, 4, 1]
res = [24, 12, 8, 6]
if it is first number in array, then input 1
in second case, if it is last number in array, input 1
i = 0, 1
nums[i] = 1, 2
len(nums) = 4, i = 3 -> 0 , -1-------- i = 2
post = [1,1,1,1]
''' 