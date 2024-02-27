# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            if not node:
                return 0
            # Count the current node if it is a "good" node
            count = 1 if node.val >= max_val else 0
            # Update the maximum value encountered so far
            max_val = max(max_val, node.val)
            # Recursively visit left and right subtrees
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count

    # Start DFS traversal from the root with initial max value as negative infinity
        return dfs(root, float('-inf'))
#         queue = []
#         pathtoleaf = []
        
#         queue.append((root,[]))
        
#         while queue:
#             node,path=queue.pop(0)
#             if node.left:
#                 queue.append((node.left,path+[node]))
#             if node.right:
#                 queue.append((node.right,path+[node]))
#             if not node.left and not node.right:
#                 pathtoleaf.append((path+[node]))
        
        
        
#         res=set()
#         for path in pathtoleaf:
#             for j in range(len(path)-1,-1,-1):
#                 flag=True
#                 for i in range(j-1,-1,-1):
#                     if path[j].val<path[i].val:
#                         flag=False
#                         break
#                 if flag:
#                     res.add(path[j])
           
#         return len(res)
                        
        