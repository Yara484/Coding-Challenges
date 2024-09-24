class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1  # Start with the first unique element at index 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:  # If current element is different from the last unique one
                nums[k] = nums[i]       # Place it in the next position for unique elements
                k += 1                  # Increment the unique count

        return k
