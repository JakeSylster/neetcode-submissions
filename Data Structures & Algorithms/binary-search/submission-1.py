# My solution not binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        index = -1
        
        if target in nums:
            index = nums.index(target)

        return index
        
#Learning Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            middle = l + ((r - l) // 2)                   #  <- same as ((l + r ) // 2 )      # // -> removes remainder 
            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle
        return -1


        