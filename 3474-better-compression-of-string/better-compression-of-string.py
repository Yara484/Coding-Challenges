class Solution:
    def betterCompression(self, compressed: str) -> str:
        from collections import defaultdict

        freq_map = defaultdict(int)
        
        i = 0
        while i < len(compressed):
            char = compressed[i]
            i += 1
            freq_str = ''
            while i < len(compressed) and compressed[i].isdigit():
                freq_str += compressed[i]
                i += 1
            freq_map[char] += int(freq_str)
        
        result = ''
        for char in sorted(freq_map):
            result += char + str(freq_map[char])
        
        return result