class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for number in nums:

            if number in seen:
                seen[number]+= 1
            else:
                seen[number] = 1
            
            if seen[number] > 1:
                return True
        return False 

        