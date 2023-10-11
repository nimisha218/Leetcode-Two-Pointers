class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        print("Nums: ", nums)

        result = []
        result_set = set()


        for i in range(len(nums)):

            first = nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                
                # print("First: ", first)
                # print("Left: ", nums[left])
                # print("Right: ", nums[right])

                if first + nums[left] + nums[right] == 0:
                    if (first, nums[left], nums[right]) not in result_set:
                        result.append([first, nums[left], nums[right]])
                        result_set.add((first, nums[left], nums[right]))
                    left = left + 1

                
                elif first + nums[left] + nums[right] > 0:
                    right = right - 1
                
                else:
                    left = left + 1

    
        return result






        return []

        
























        
        # nums.sort()
        # result = []
        # print("Nums sorted: ")
        # print(nums)

        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i - 1]:
        #         continue
        #     left = i + 1
        #     right = len(nums) - 1

        #     while left < right:
        #         if a + nums[left] + nums[right] == 0:
        #             result.append([a, nums[left], nums[right]])
        #             left = left + 1
        #             while nums[left] == nums[left-1] and left < right:
        #                 left = left + 1
        #         elif a + nums[left] + nums[right] > 0:
        #             right = right - 1
        #         else:
        #             left = left + 1
        
        # return result

