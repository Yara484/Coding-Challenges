class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}

        for word in strs:
            Sword = sorted(word)
            Sword = "".join(Sword)
            if Sword in myMap:
                myMap[Sword].append(word)
            else:
                myMap[Sword] = [word]

        return myMap.values()            
            