class Solution:
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


        