#Using loops

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

#Using hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, number in enumerate(nums):

            diff = target - number

            if diff in hashmap:
                return [hashmap[diff], index]

            hashmap[number] = index