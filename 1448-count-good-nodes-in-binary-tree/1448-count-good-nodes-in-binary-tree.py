# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = []
        pathtoleaf = []
        
        queue.append((root,[]))
        
        while queue:
            node,path=queue.pop(0)
            if node.left:
                queue.append((node.left,path+[node]))
            if node.right:
                queue.append((node.right,path+[node]))
            if not node.left and not node.right:
                pathtoleaf.append((path+[node]))
        
        
        
        res=set()
        for path in pathtoleaf:
            for j in range(len(path)-1,-1,-1):
                flag=True
                for i in range(j-1,-1,-1):
                    if path[j].val<path[i].val:
                        flag=False
                        break
                if flag:
                    res.add(path[j])
           
        return len(res)
                        
        