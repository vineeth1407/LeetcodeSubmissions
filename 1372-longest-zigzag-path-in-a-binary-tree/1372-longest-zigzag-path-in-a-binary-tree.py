# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxlen = 0
    def solve(self,root,curlen,direction):
        if not root:
            return 
        self.maxlen = max(self.maxlen,curlen)
        
        self.solve(root.left,0,curlen+1 if direction else 1)
        self.solve(root.right,1,1 if direction else curlen+1)
        
        
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        self.maxlen = 0
        # root is a TreeNode, direction is an integer which is either 0(left) or 1(right) and curr_len is current length which is an integer
        def traverse(root, direction, curr_len):
            if not root:
                return
            self.maxlen = max(self.maxlen, curr_len)

            traverse(root.left, 0, curr_len+1 if direction else 1)
            traverse(root.right, 1, 1 if direction else curr_len+1)

        traverse(root, 0, 0)
        return self.maxlen
        
                
        