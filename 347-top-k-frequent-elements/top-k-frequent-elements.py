class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency Array
        # Create array with length of nums
        farray = [[] for i in range(len(nums)+1)]
        mymap = {}
        res = []
        # Hashmap of values and their frequencies
        for i in nums:
            mymap[i] = mymap.get(i, 0) + 1
        # Populating Freq array
        for key, value in mymap.items():
            farray[value].append(key)  
        # Building result string by iterating in reverse
        for i in range(len(farray)-1, 0, -1):
            for j in farray[i]:
                res.append(j) 
                if len(res) == k:
                    return res