class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0]* numCourses
        adj_matrix = {}
        for i in prerequisites:
            adj_matrix[i[0]] = adj_matrix.get(i[0],[])
            adj_matrix[i[0]].append(i[1])
        
        course_order = []

        def dfs_util(v):
            visited[v]=2
            if v in adj_matrix:
                for i in adj_matrix[v]:
                    if visited[i]==2:
                        return False
                    
                    elif visited[i]!=1 and dfs_util(i)==False:
                        return False
                    
            visited[v]=1
            course_order.append(v)
            return True
        
        for i in range(numCourses):
            if visited[i]==0 and dfs_util(i)==False:
                return []
        
        return course_order