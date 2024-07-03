class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        farray = [[] for i in range(len(nums) + 1)]

        res = []
        for i in nums:
            count[i] = count.get(i, 0) + 1  

        for num, freq in count.items():
            farray[freq].append(num)   

        for i in range(len(farray)-1, 0, -1):
            for n in farray[i]:
                res.append(n)
                if len(res) == k:
                    return res