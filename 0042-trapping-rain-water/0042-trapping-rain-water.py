class Solution:
    def trap(self, height: List[int]) -> int:

        total_amount = 0
        curr_max = 0

        max_left = [0 for i in range(len(height))]
        max_right = [0 for i in range(len(height))]
        min_height = [0 for i in range(len(height))]

        for i in range(len(height)):
            if i == 0:
                continue
            if height[i-1] >= curr_max:
                max_left[i] = height[i-1]
                curr_max = height[i-1]
            else:
                max_left[i] = curr_max
        
        curr_max = 0

        for i in range(len(height)-1, -1, -1):
            if i == len(height) - 1:
                continue
            if height[i+1] >= curr_max:
                max_right[i] = height[i+1]
                curr_max = height[i+1]
            else:
                max_right[i] = curr_max

        for i in range(len(height)):
            amount = min(max_left[i], max_right[i]) - height[i]
            if amount > 0:
                total_amount = total_amount + amount

        return total_amount

            
        
        

            

            
            






    

            
            



            
            
        