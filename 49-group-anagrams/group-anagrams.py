class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a  hashmap to store char frequency
        # key is sorted string
        mymap = {}
        for word in strs:
            Sword = sorted(word) # ['a', 'c', 't']
            Sword = ''.join(Sword)      # 'act'
            if Sword in mymap:
                mymap[Sword].append(word)
            else:
                mymap[Sword] = [word]  

        # Now I have to build the result array
        res = []
        for i in mymap:
            res.append(mymap[i])
        return res              
    