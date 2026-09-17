#My solution
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         listofwords = []
#         listofwords = s.split()
#         return (len(listofwords[-1]))

#Video solution
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         i = len(s) -1
#         length = 0

#         while s[i] == " ":
#             i -= 1
#         while i >= 0 and s[i] != " ":
#             length += 1
#             i -= 1
#         return length

#Manoj solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        i = -1
        if len(s) == 1 and s != " ":
            return 1

        while s[i] == " ":
            i -= 1
            
        k = len(s) + i
        
        for j in range(k,-1,-1):
            if s[j] == " " or j == 0:
                return counter
            counter += 1