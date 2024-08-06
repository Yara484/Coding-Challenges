class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Using two pointers
        # area = width * height
        res = 0
        l, r = 0, len(height)-1

        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            if height[r] > height[l]:
                l += 1
            else:
                # This also takes care of the special case of equal heights
                r -= 1
        return res            