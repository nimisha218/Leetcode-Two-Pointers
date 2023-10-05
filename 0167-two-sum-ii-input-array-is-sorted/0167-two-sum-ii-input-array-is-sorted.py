class Solution:
    def twoSum(self, numbers, target):

        left = 0
        right = len(numbers) - 1

        while left <= right:

            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            
            # If the sum is greater than target, we need to decrease the right pointer 
            if numbers[left] + numbers[right] > target:
                right = right - 1
                
            # If the sum is lesser than target, we need to increase the left pointer 
            else:
                left = left + 1
        





























        # answer = []

        # for i in range(len(numbers)):
        #     if numbers[i] == 0 and target != 0:
        #         if i < len(numbers) and numbers[i+1] == 0:
        #             continue
        #     if numbers[i] < 0 and numbers[i+1] < 0 and target > 0:
        #         continue

        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             answer.append(i+1)
        #             answer.append(j+1)
        #             return answer