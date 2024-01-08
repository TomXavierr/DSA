"""Range Sum of BST"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            current = 0
            if low<= node.val <= high:
                current = node.val
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            return current + left_sum + right_sum
        
        return dfs(root)
