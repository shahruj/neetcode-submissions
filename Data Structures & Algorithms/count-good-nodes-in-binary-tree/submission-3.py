# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs


from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_so_far = root.val
        queue = deque()
        queue.append((root,max_so_far))
        
        n = 0
        while queue:
            node, max_so_far = queue.popleft()

            if node.val >= max_so_far:
                n += 1

            max_so_far = max(max_so_far, node.val)

            if node.left:
                queue.append((node.left, max_so_far))

            if node.right:
                queue.append((node.right, max_so_far))

        return n



        
        