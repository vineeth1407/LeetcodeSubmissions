class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       
        visited = [0]* numCourses
        adj_matrix = {}
        for i in prerequisites:
            adj_matrix[i[0]] = adj_matrix.get(i[0],[])
            adj_matrix[i[0]].append(i[1])

        
        def dfs_util(v):
            visited[v]=2
            if v in adj_matrix:
                for i in adj_matrix[v]:
                    if visited[i]==2:
                        return False
                    
                    elif visited[i]!=1 and dfs_util(i)==False:
                        return False
            visited[v]=1  
            return True
        
        #print(adj_matrix)
        for i in range(numCourses):
            if visited[i]==0 and dfs_util(i)==False:
                return False
        
        return True
        