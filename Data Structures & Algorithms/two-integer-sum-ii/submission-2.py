class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index,number in enumerate(numbers):
            remaining = target - number
            if remaining in seen:
                first = seen[remaining]
                return [first+1,index+1]
            seen[number] = index
        # for i in range(0,len(numbers)-1):
        #     if numbers[i] + numbers[i+1] == target:
        #         return [i+1,i+2]
