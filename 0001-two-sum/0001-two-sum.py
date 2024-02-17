class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        orig = nums.copy()
        nums.sort()
        l=0
        h = len(nums)-1
        res = []


        while l<h:
            if nums[l]+nums[h]==target:
                res.append(nums[l])
                res.append(nums[h])
                break
            elif nums[l]+nums[h]<target:
                l+=1
            else:
                h-=1
       # print(res)
        ans = []
        for i in range(len(nums)):
            if orig[i] ==res[0] or orig[i]==res[1]:
                ans.append(i)
        return ans

        