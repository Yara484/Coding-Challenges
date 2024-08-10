class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Creating maxHeap from minHeap
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap) # First largest value
            stone2 = heapq.heappop(maxHeap) # Second largest value
            # stone1 - stone2 but reversing the logic
            smash = stone1 - stone2
            if stone2 > stone1:
                heapq.heappush(maxHeap, smash)

        if len(maxHeap) == 1:
            return -heapq.heappop(maxHeap)  
        else:
            return 0          