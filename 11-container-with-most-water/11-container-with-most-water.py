class Solution:
    def maxArea(self, height) -> int:
        n = len(height)
        right = n-1 #index 
        left = 0
        maxArea = 0
        
        while right > left:
            if height[left] <= height[right]:
                maxArea = max(maxArea,min(height[left],height[right]) * (right-left))
                left += 1
            else:
                maxArea = max(maxArea,min(height[left],height[right]) * (right-left))
                right -= 1
        
        return maxArea  
