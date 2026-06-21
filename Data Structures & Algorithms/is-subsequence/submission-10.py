class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s1 = t1 = 0

        for t1 in range(len(t)):
            if s1 < len(s) and s[s1] == t[t1]:
                s1 += 1
            
        return s1 == len(s)                

        