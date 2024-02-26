class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        window_sum = None
        for i in range(0,len(nums)-k+1):
            if not window_sum:
                window_sum = sum(nums[i:i+k])
            else:
                window_sum  = window_sum + nums[i+k-1] - nums[i-1]
            
            max_avg = max(max_avg,window_sum/k)
        
        return max_avg
                
            
        