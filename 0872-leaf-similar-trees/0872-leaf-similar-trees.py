# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def BFS(self,root):
        if not root:
            return root
        ans = []
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            if not cur.left and not cur.right:
                ans.append(cur.val)
        return ans
    
    def DFS(self,root,ans):
        if not root:
            return
        if not root.left and not root.right:
            ans.append(root.val)
        self.DFS(root.left,ans)
        self.DFS(root.right,ans)
        
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        self.DFS(root1,l1)
        self.DFS(root2,l2)
        print(l1)
        print(l2)
        return l1==l2
        