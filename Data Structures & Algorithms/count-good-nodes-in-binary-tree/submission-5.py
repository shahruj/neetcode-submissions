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
            lenq = len(queue)
            for i in range(0,lenq):
                curr = queue.popleft() 
                if curr[0]:
                    if curr[0].val >= curr[1]:
                        n+=1
                    max_so_far = max(curr[1], curr[0].val)
                    if curr[0].left:
                        queue.append((curr[0].left,max_so_far))
                    if curr[0].right:
                        queue.append((curr[0].right,max_so_far))
                    
        return n
                        



        
        