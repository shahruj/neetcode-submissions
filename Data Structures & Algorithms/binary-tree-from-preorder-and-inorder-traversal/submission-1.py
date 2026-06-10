# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        root = TreeNode(preorder[0])
        
        idxroot = inorder.index(root.val)
        leftsideinorder = inorder[:idxroot]
        rightsideinorder = inorder[idxroot+1:]

        leftpreorder = [x for x in preorder if x in leftsideinorder]
        rightpreorder = [x for x in preorder if x in rightsideinorder]

        root.left = self.buildTree(leftpreorder,leftsideinorder)
        root.right = self.buildTree(rightpreorder,rightsideinorder)

        return root




        