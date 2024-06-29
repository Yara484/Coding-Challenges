class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = {}
        for word in strs:
            wordS = "".join(sorted(word))
            if wordS not in mymap:
                mymap[wordS] = [word]
            else:
                mymap[wordS].append(word)     
        return mymap.values()