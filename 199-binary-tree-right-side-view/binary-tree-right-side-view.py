# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            right = None
            for i in range(len(q)):
                node = q.popleft()
                right = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(right.val) if right else None
        return res            
              