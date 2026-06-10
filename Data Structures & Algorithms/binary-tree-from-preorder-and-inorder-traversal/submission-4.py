# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.map = {}
        for idx,i in enumerate(preorder):
            self.map[i] = idx

        def dfs(preorder,inorder):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            idxroot = inorder.index(root.val)
            leftsideinorder = inorder[:idxroot]
            rightsideinorder = inorder[idxroot+1:]

            leftsidepreorder = sorted(
                leftsideinorder,
                key=lambda x: self.map[x]
            )
            rightsidepreorder = sorted(
                rightsideinorder,
                key=lambda x: self.map[x]
            )

            root.left = dfs(leftsidepreorder,leftsideinorder)
            root.right = dfs(rightsidepreorder,rightsideinorder)

            return root

        return dfs(preorder,inorder)

# class Solution:
#     def buildTree(self, preorder, inorder):

#         inorder_map = {v:i for i,v in enumerate(inorder)}
#         preorder_idx = 0

#         def dfs(left, right):
#             nonlocal preorder_idx

#             if left > right:
#                 return None

#             root_val = preorder[preorder_idx]
#             preorder_idx += 1

#             root = TreeNode(root_val)

#             mid = inorder_map[root_val]

#             root.left = dfs(left, mid - 1)
#             root.right = dfs(mid + 1, right)

#             return root

#         return dfs(0, len(inorder) - 1)


        