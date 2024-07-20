# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0

        def maxDepth(root):
            nonlocal max_d
            
            if not root:
                return 0

            left = maxDepth(root.left)
            right = maxDepth(root.right)

            d = left + right
            max_d = max(max_d, d)

            return 1 + max(left, right)

        maxDepth(root)
        return max_d        