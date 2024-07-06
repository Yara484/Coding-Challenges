class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        map2 = {}
        l = 0

        for char in s1:
            map1[char] = map1.get(char, 0) + 1

        for r in range(len(s2)):
            map2[s2[r]] = map2.get(s2[r] , 0) + 1

            if r >= len(s1):
                if map2[s2[l]] == 1:
                    del map2[s2[l]]
                else: 
                    map2[s2[l]] -= 1
                l += 1
            if map1 == map2: return True
        return False