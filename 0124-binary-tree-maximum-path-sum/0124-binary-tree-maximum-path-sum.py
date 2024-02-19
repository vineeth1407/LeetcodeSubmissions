# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root
        
        max_sum = float("-inf")
        
        def maxpathsum_util(root):
            nonlocal max_sum
            if not root:
                return 0
            
            left_sum = max(0, maxpathsum_util(root.left))
            right_sum = max(0,maxpathsum_util(root.right))
            
            
            total_sum = root.val + left_sum +right_sum
            max_sum = max(max_sum,total_sum)
            
            return max(left_sum,right_sum)+root.val
        
        
        maxpathsum_util(root)
        return max_sum
        