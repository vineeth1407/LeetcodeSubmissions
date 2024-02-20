import sys
sys.setrecursionlimit(10**6)
 
class Solution:
    def recursion(self,nums,index,target):
        if target==0:
            return True
        
        if index==0:
            return nums[index]==target
        
        notTake = self.recursion(nums,index-1,target)
        Take = False
        
        if nums[index]<=target:
            Take = self.recursion(nums,index-1,target-nums[index])
            
        return notTake or Take
    
    
    
    def dpapproach(self,nums,target):
        n = len(nums)
        dp = [[False for j in range(target+1)] for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=True
        
        for i in range(1,target+1):
            dp[0][i]= False
        
        for i in range(1,n+1):
            for j in range(1,target+1):
                if j<nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
        return dp[n][target]
    
    
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2!=0:
            return False
        required_sum = total_sum//2
        
        #return self.recursion(nums,len(nums)-1,required_sum)
        return self.dpapproach(nums,required_sum)
        