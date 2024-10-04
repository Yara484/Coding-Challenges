class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Using min heap
        myMap = {}

        for ids, score in items:
            if ids not in myMap:
                myMap[ids] = []
            heapq.heappush(myMap[ids], score)
            if len(myMap[ids]) > 5:
                heapq.heappop(myMap[ids])    

        res = []
        for key, value in myMap.items():
            res.append([key, sum(value) // 5])   
        
        res.sort()
        return res         