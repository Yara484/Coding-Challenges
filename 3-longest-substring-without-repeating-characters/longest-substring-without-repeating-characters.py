class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window using a set because it can only store unique characters
        myset = set()
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] in myset:
                myset.remove(s[l])
                l += 1
            else:
                myset.add(s[r])
                length = r - l + 1
                res = max(res, length)
                r += 1
        return res        