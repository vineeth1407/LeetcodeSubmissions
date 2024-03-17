class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        k =0
        l =0
        
        while k<m and l<n:
            
            for i in range(l,n):
                ans.append(matrix[k][i])
            
            k+=1
            
            for i in range(k,m):
                ans.append(matrix[i][n-1])
            
            n-=1
            
            if k<m:
                for i in range(n-1,(l-1),-1):
                    ans.append(matrix[m-1][i])
            m-=1
            
            
            if l<n:
                for i in range(m-1,(k-1),-1):
                    ans.append(matrix[i][l])
            l+=1
        
        return ans
            
            