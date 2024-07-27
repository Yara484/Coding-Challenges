# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, minB, maxB):
            if not root:
                return True
            if not (root.val > minB and root.val < maxB):
                return False

            return validate(root.left, minB, root.val) and validate(root.right, root.val, maxB) 

        return validate(root, float('-inf'), float('inf'))          