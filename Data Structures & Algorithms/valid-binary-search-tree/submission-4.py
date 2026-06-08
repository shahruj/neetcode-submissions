# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def dfs(node, low, high):
#             if not node:
#                 return True

#             if not (low < node.val < high):
#                 return False

#             return (
#                 dfs(node.left, low, node.val) and
#                 dfs(node.right, node.val, high)
#             )


#         return dfs(root, float("-inf"), float("inf"))


from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque()
        queue.append((root, float("-inf"), float("inf")))

        while queue:
            node, low, high = queue.popleft()

            if not (low < node.val < high):
                return False

            if node.left:
                queue.append((node.left, low, node.val))

            if node.right:
                queue.append((node.right, node.val, high))

        return True
        