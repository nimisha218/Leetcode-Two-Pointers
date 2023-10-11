import math

class Solution:
    def maxArea(self, height: List[int]) -> int:
 
        left = 0
        right = len(height) - 1
        max_amount = 0

        while left < right:
            
            if height[left] < height[right]:
                amount = height[left] * (right - left)
                left = left + 1
            
            else:
                amount = height[right] * abs(left - right)
                right = right - 1
   
            if amount >= max_amount:
                max_amount = amount

        
        return max_amount