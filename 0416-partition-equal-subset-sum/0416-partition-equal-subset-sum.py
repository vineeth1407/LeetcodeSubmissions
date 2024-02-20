import sys
sys.setrecursionlimit(10**6)
 
class Solution:
    def Recursion(self,nums,index,target):
        if target==0:
            return True
        
        if index==0:
            return nums[index]==target
        
        notTake = self.recursion(nums,index-1,target)
        Take = False
        
        if nums[index]<=target:
            Take = self.recursion(nums,index-1,target-nums[index])
            
        return notTake or Take
    
    
    
    def DpApproach(self,nums,target):
        n = len(nums)
        dp = [[False for j in range(target+1)] for i in range(n+1)]
        
        # if target is zero, it is true for every index
        for i in range(n+1):
            dp[i][0]=True
        
        # if index is 0 and we still have target , it cannot be achieved
        for i in range(1,target+1):
            dp[0][i]= False
        
        #bottom-up approach
        for i in range(1,n+1):
            for j in range(1,target+1):
                if j<nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
        return dp[n][target]
    
    
    def DPSpaceOptimized(self,nums,target):
        n = len(nums)
        dp = [False] * (target+1)
        
        #if target is zero, it is true
        dp[0]= True
        
        for i in range(1,n+1):
            cur = [False]*(target+1)
            for j in range(1,target+1):
                if j<nums[i-1]:
                    cur[j] = dp[j]
                else:
                    cur[j] = dp[j] or dp[j-nums[i-1]]
            dp = cur
    
        
        return dp[target]
        
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2!=0:
            return False
        required_sum = total_sum//2
        
        #return self.Recursion(nums,len(nums)-1,required_sum)
        
        #return self.DpApproach(nums,required_sum)
        
        return self.DPSpaceOptimized(nums,required_sum)
        