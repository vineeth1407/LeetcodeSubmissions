class Solution:
    def approach1(self,nums):
        left_sum = [0] * len(nums)
        right_sum = [0]* len(nums)
        
        for i in range(1,len(nums)):
            left_sum[i] = left_sum[i-1] +nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            right_sum[i] = right_sum[i+1] +nums[i+1]
        
        # print(left_sum)
        # print(right_sum)
        for i in range(len(nums)):
            if left_sum[i]==right_sum[i]:
                return i
        return -1
    
    def pivotIndex(self, nums: List[int]) -> int:
          total_sum = sum(nums)
          left_sum = 0
          index = -1
          for i in range(len(nums)):
              right_sum = total_sum - nums[i]
              if left_sum == right_sum:
                 index =i
                 break
              left_sum +=nums[i]
              total_sum-= nums[i]
          return index


        