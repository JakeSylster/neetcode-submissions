# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = {}
        # for index,number in enumerate(nums):
        #     remaining = target - number
        #     if remaining in seen:
        #         return([seen[remaining],index])
        #     seen[number]=index

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,number in enumerate(nums):
            remaining = target - number
            if remaining in seen:
                return([seen[remaining],index])
            seen[number] = index