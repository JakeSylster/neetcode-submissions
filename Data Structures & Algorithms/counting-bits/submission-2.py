#Brute force, self written, first attempt finish
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ones = []

        for i in range(n+1):
            binary = bin(i)
            counter = 0
            for j in str(binary):
                if j == "1":
                    counter += 1
            ones.append(counter)
        return ones


#Video explanation implementation
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n+1)
        offset = 1

        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[ i - offset ]
        
        return dp


        