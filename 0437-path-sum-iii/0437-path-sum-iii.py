# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def path_sum_util(self,root,Sum):
        if not root:
            return 0

        res=0

        if root.val==Sum: 
            res+=1

        res+=self.path_sum_util(root.left,Sum-root.val)
        res+=self.path_sum_util(root.right,Sum-root.val)
        return res

        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if not root:
            return 0
        return self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)+ self.path_sum_util(root,targetSum)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                    
#         q = []
#         paths_to_leaf = []
        
#         q.append((root,[]))
        
#         while q :
#             node,path = q.pop(0)
            
#             if node.left:
#                 q.append((node.left,path+[node]))
            
#             if node.right:
#                 q.append((node.right,path+[node]))
            
#             if not node.left and not node.right:
#                 paths_to_leaf.append(path+[node])
        
#         res = set()
#         for path in paths_to_leaf:
#             for j in range(len(path)):
#                 for i in range(j,len(path)):
#                     if path[i].val+path[j].val==k:
#                         res.append(
        
        return 5
        
        
        