class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a max heap
        nums = [-i for i in nums]
        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k -= 1
        # minus it to get max element
        return -heapq.heappop(nums)    