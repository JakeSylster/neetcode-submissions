class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        result = 0

        for num in nums:
            if num == 0:
                result = max(result,counter)
                counter = 0
            else:
                counter += 1

        return max(counter,result)

        