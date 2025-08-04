"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""

# Runtime : 0ms , Beats 100.00%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
    
        left_queue = deque([root.left])
        right_queue = deque([root.right])

        while left_queue and right_queue : 
            
            l_node = left_queue.popleft()
            r_node = right_queue.popleft()

            if not l_node and not r_node:
                continue
            
            if not l_node or not r_node or l_node.val != r_node.val:
                return False 
            
            left_queue.append(l_node.left)
            right_queue.append(r_node.right)
            right_queue.append(r_node.left)
            left_queue.append(l_node.right)

        return  not left_queue and not right_queue
            
