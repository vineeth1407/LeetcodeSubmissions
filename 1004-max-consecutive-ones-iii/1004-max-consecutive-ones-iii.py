class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_ones = 0
        count_dict = {1:0,0:0}
        
        for right in range(0,len(nums)):
            count_dict[nums[right]]+=1
            
            while count_dict[0]>k:
                count_dict[nums[left]]-=1
                left+=1
            
            ones = right-left+1
            max_ones = max(ones,max_ones)
        
        return max_ones