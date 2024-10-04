class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqMap = {}
        
        for char in s:
            freqMap[char] = freqMap.get(char, 0) + 1

        for i, char in enumerate(s):
            if freqMap[char] == 1:
                return i    
                
        return -1              

                