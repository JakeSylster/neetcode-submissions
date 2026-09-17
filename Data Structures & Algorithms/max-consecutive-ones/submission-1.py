# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         counter = 0
#         result = 0

#         for num in nums:
#             if num == 0:
#                 result = max(result,counter)
#                 counter = 0
#             else:
#                 counter += 1

#         return max(counter,result)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        result = 0
        for number in nums:
            if number == 1:
                counter +=1
            else:
                counter = 0
            result = max(counter,result)
        return result
            