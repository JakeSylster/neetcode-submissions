#Brute force self written first attempt finish
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


