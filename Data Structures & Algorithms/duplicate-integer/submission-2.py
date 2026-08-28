class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        fake = []
        for number in nums:
            a = number
            if a in fake:
                return True
            fake.append(a)
        return False


