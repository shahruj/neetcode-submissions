# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
#         def check(root):
#             if not root:
#                 return 0  # height = 0
            
#             left = check(root.left)
#             if left == -1:
#                 return -1
            
#             right = check(root.right)
#             if right == -1:
#                 return -1
            
#             if abs(left - right) > 1:
#                 return -1
            
#             return 1 + max(left, right)
        
#         return check(root) != -1






# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:

#         def dfs(node):
#             if not node:
#                 return 0, True

#             left, balanced_left = dfs(node.left)
#             right, balanced_right = dfs(node.right)

#             balanced = balanced_left and balanced_right and abs(left-right)<=1

#             if balanced:
#                 return 1+max(left,right), True
#             else:
#                 return None, False

#         depth, balanced  = dfs(root)
#         return balanced































class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0, True
            
            left, left_balanced = dfs(node.left)
            right, right_balanced = dfs(node.right)

            if left_balanced and right_balanced and abs(left-right)<=1:
                return 1+max(left,right), True
            else:
                return 1+max(left,right), False

            
        maxDepth, balanced = dfs(root)

        return balanced

































