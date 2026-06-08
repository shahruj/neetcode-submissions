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

            for i in range(0,length_of_queue):
                curr = queue.popleft()
                temp_arr = []
                if curr.val:
                    temp_arr.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            print(temp_arr)
            if temp_arr:
                result.append(temp_arr[-1])
        
        return result


