# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtree(self,root):
        ans = [root.val]
        return ans
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        while root:
            # print("ll")
            if root.val==val:
                return root
                # return self.subtree(root)
            elif root.val<val:
                root = root.right
            else:
                root = root.left
        return None
        