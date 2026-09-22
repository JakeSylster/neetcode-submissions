class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        counter = 0
        nums.sort()
        print(nums)
        if len(nums) == 0:
            return 0
        for index in range(1,len(nums)):
            # print(counter)
            if nums[index]==nums[index-1]:
                continue
            elif nums[index]-nums[index-1] == 1:
                counter += 1
            else:
                counter = 0
            result = max(result,counter)
            # print("r=",result)
        return  result + 1