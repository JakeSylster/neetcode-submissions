import itertools
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Best as per video
        result = []
        nums.sort()
        for index,number in enumerate(nums):
            if index > 0 and number == nums[index-1]:
                continue

            l,r = index+1 , len(nums)-1
            while l<r:
                totalSum = number + nums[l] + nums[r]
                if totalSum > 0:
                    r -= 1
                elif totalSum < 0:
                    l += 1
                else:
                    result.append([number,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result

        #Subsets version , Big memory needed
        # total=0
        # new_list=[]
        # nums = list(set(nums))
        # nums = sorted(nums)
        # subsets = set(itertools.combinations(nums, 3))
        # for item in subsets:
        #     for number in item:
        #         total+=number
        #     item=list(item)
        #     if total == 0:
        #         new_list.append(item)
        #     total =0
        # return new_list

        #Brute Force
        # result = []
        # nums.sort()
        # print(nums)
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if i <= 1:
        #                 if nums[i] + nums[j] + nums[k] == 0:
        #                     new_element = sorted([nums[i],nums[j],nums[k]])
        #                     if new_element not in result:
        #                         result.append([nums[i],nums[j],nums[k]])
        # return result
                
          