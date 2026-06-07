# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return same(a.left, b.left) and same(a.right, b.right)

        def dfs(node, subRoot):
            if not subRoot:
                return True
            if not node:
                return False
            if same(node, subRoot):
                return True

            return dfs(node.left,subRoot) or dfs(node.right,subRoot)

        return dfs(root, subRoot)
        