class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hashmap that counts no. of occurences of each number
        countMap = {}
        arr = []
        res = []
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1

        for num, count in countMap.items():
            arr.append([count, num])
        arr.sort(reverse = True)

        for i in range(k):
            res.append(arr[i][1])

        return res 