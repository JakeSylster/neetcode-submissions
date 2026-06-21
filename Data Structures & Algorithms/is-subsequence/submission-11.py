#Brute force, self written, claude assited in problem finding, Not solution
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
        
#         s1 = t1 = 0

#         for t1 in range(len(t)):
#             if s1 < len(s) and s[s1] == t[t1]:
#                 s1 += 1
            
#         return s1 == len(s)                

#Video Solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return True if i == len(s) else False


        