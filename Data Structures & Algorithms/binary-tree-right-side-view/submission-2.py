# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# check if there is nothing to the right of something 

from collections import deque
queue = deque()
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue.append(root)

        while queue:
            length_of_queue = len(queue)
            temp_arr = []
            for i in range(0,length_of_queue):
                curr = queue.popleft()
                if curr:
                    temp_arr.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
      
            if temp_arr:
                result.append(temp_arr[-1])
        
        return result


