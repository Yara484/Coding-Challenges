class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        myMap = {}

        for ids, score in items:
            if ids not in myMap:
                myMap[ids] = []
            myMap[ids].append(score)    
        
        for key, value in myMap.items():
            value.sort(reverse=True)  
        total = 0
        i = 0
        res = []
        for key, value in myMap.items():
            while i < 5:
                total += value[i]
                i += 1
            res.append([key, total // 5])    
            i = 0
            total = 0
        res.sort()    
        return res    
