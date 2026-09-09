import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fake = nums
        output = []
        if 0 in nums:
            output = [0]*(len(nums)-1)
            loc= fake.index(0)
            fake.remove(0)
            total = math.prod(fake)
            output.insert(loc,total)
            return output
        else:
            total = math.prod(nums)
            for i in range(0,len(nums)):
                    number = total / nums[i]
                    output.append(int(number))
                
        return output