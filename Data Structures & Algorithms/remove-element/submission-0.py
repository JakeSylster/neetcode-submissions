class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # counter = 0
        # for index,number in enumerate(nums):
        #     if number == val:
        #         counter += 1
        #         print(f"c={counter}")
        #         nums.pop(index)
        #         # del nums[index]
        #         index -= 1
        #         # print(f"popped={nums}")
        #         nums.append("_")
        # k = len(nums)-counter
        # print(f"k={k}")
        # print(f"nums={nums}")
        # return k
        count = nums.count(val)
        k = len(nums)- count
        
        for i in range(count):
            nums.remove(val)
            nums.append("_")
        return k