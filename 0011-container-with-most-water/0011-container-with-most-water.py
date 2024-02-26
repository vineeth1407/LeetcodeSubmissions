class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        l , h = 0,n-1
        
        while l<h:
            cur_area = min(height[l],height[h]) * (h-l)
            max_area = max(max_area,cur_area)
            
            if height[l]<height[h]:
                l+=1
            else:
                h-=1
        return max_area
        