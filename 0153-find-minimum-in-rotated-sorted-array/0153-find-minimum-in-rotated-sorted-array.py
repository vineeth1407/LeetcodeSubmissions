class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        if len(nums)==1:
            return nums[0]
        if nums[high]>nums[low]:
            return nums[low]
        
        while low<=high:
            mid = (low+high)//2
            
            
            if mid+1<len(nums) and nums[mid]>nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            
            if nums[mid]>nums[low]:
                low= mid+1
            else:
                high = mid-1
    
    
        return -1
        
        