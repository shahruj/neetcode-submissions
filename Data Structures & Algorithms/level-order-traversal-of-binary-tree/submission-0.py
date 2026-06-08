# Definition for a binary tree node.
from typing import *
from collections import *
from heapq import *
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
            


# ----------------------
# Test Case 1
#     3
#    / \
#   9  20
#      / \
#     15  7
# Expected: [[3],[9,20],[15,7]]
# ----------------------
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(Solution().levelOrder(root1))


# ----------------------
# Test Case 2
# Empty tree
# Expected: []
# ----------------------
root2 = None

print(Solution().levelOrder(root2))


# ----------------------
# Test Case 3
# Single node
#     1
# Expected: [[1]]
# ----------------------
root3 = TreeNode(1)

print(Solution().levelOrder(root3))


# ----------------------
# Test Case 4
#       1
#      / \
#     2   3
#    /   / \
#   4   5   6
# Expected: [[1],[2,3],[4,5,6]]
# ----------------------
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.right = TreeNode(3)
root4.left.left = TreeNode(4)
root4.right.left = TreeNode(5)
root4.right.right = TreeNode(6)

print(Solution().levelOrder(root4))