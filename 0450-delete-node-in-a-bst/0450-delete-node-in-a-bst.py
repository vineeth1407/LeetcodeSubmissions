# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self,node):
        # Helper function to find the minimum node in a subtree
        while node.left:
            node = node.left
        return node
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found, handle deletion cases
            if not root.left:  # Node has no left child
                return root.right
            elif not root.right:  # Node has no right child
                return root.left
            else:
                # Node has two children, find the minimum value in the right subtree
                min_node = self.findMin(root.right)
                root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
    
        return root
        