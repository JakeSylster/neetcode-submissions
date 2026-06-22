#Brute force
class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        for i in list(bin(n)):
            if i == "1":
                ones += 1
        return ones
        
#Using Counters
from collections import Counter
class Solution:
    def hammingWeight(self, n : int) -> int:

        count = Counter(list(bin(n)))

        return count["1"]

#Using video solution - bit manipulation
class Solution:
    def hammingWeight(self, n : int) -> int:
        res = 0

        while n:
            res += n % 2
            n = n >> 1

        return res
         
#Using video solution - bitwise AND manipulation
class Solution:
    def hammingWeight(self, n : int) -> int:
        res = 0

        while n:
            n &= (n-1)
            res += 1             

        return res