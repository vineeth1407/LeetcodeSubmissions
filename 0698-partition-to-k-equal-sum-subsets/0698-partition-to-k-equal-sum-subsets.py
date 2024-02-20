class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        
        if total_sum % k != 0:
            return False
        
        target_sum = total_sum // k
        max_num = max(nums)
        
        if max_num > target_sum:
            return False
        
        nums.sort(reverse=True)  # Sort in descending order
        
        visited = [False] * n
        
        def backtrack(start_index, cur_sum, num_sets):
            if num_sets == k - 1:
                return True
            
            if cur_sum == target_sum:
                return backtrack(0, 0, num_sets + 1)
            
            for i in range(start_index, n):
                if not visited[i] and cur_sum + nums[i] <= target_sum:
                    visited[i] = True
                    if backtrack(i + 1, cur_sum + nums[i], num_sets):
                        return True
                    visited[i] = False
                # elif cur_sum + nums[i] > target_sum:
                #     break  # Stop exploring further if current subset sum exceeds target sum
            
            return False
        
        return backtrack(0, 0, 0)
#         n = len(nums)
        
#         if sum(nums)%k!=0:
#             return False
        
#         max_ele = max(nums)
#         target_sum = sum(nums)//k
#         if max_ele>target_sum:
#             return False
#         # if target_sum<k:
#         #     return False
#         visited = [False]*n
#         nums.sort(reverse=True)
#         def helper(index,cur_sum,i):
#             if i==1:
#                 return True
#             if cur_sum>target_sum:
#                 return False
            
#             if cur_sum == target_sum:
#                 return helper(0,0,i-1)
            
#             for j in range(index,n):
#                 if visited[j]==False:
#                     # if cur_sum + nums[j] > target_sum:
#                     #     break
#                     visited[j]=True
#                     if cur_sum+nums[j]<=target_sum and helper(j+1,cur_sum+nums[j],i)==True:
#                         return True
#                     visited[j] = False
                
#             return False
        
#         return helper(0,0,k)
            
            
            
        