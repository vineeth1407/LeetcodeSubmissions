class Solution:
    def recursive_sol(self,word1,word2):
        def recur_util(i,j):
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            
            if word1[i]==word2[j]:
                return recur_util(i+1,j+1)
            add = recur_util(i,j+1)
            rem = recur_util(i+1,j)
            rep = recur_util(i+1,j+1)
            
            return min(add,rem,rep)+1
        
        return recur_util(0,0)
    
    
    def dp_sol(self,word1,word2):
        
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for i in range(m+1)]
        
        
        
        for i in range(m+1):
            dp[i][0]=i
            
        for j in range(n+1):
            dp[0][j]=j
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                    
        
        return dp[m][n]
            
    def minDistance(self, word1: str, word2: str) -> int:
       # return self.recursive_sol(word1,word2)
        return self.dp_sol(word1,word2)
        