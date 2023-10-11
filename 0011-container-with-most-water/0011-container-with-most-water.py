import math

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # for i, h in enumerate(height):
        #     print("i: ", i)
        #     print("height: ", h)
        #     print()

        left = 0
        right = len(height) - 1
        max_amount = 0

        while left < right:
            
            # print("left: ", left)
            # print("right: ", right)

            if height[left] < height[right]:
                # print("Left was shorter than right")
                amount = height[left] * (right - left)
                left = left + 1
                # right = right - 1
            
            else:
                amount = height[right] * abs(left - right)
                # print("right was shorter than left")
                right = right - 1
                # left = left + 1
        

            
            # print("amount: ", amount)

            if amount >= max_amount:
                max_amount = amount

            
            
            # print("max amount: ", max_amount)
            # print("-------------------")

            




        
        return max_amount