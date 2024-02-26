class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        count_dict = {1:0,0:0}
        
        for right in range(len(nums)):
            count_dict[nums[right]]+=1
            
            while count_dict[0]>1:
                count_dict[nums[left]]-=1
                left+=1
            cur = right-left+1
            ans = max(ans,cur)
        return ans-1