# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

queue = deque()
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

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
                result.append(temp_arr)

        return result
                                                                                                                                                                                                                                                                                                            