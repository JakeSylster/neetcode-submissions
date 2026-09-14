# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        # if (len(s)==len(t)):
        #     for i in s:
        #         if i in t:
        #             s = s.replace(i, "", 1)
        #             t= t.replace(i,"",1)
        #     if s ==  "":
        #         return True
        # return False       

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Sseen = {}
        Tseen = {}
        if len(s) == len(t):
            for i in range(0,len(s)):
                if s[i] in Sseen:
                    Sseen[s[i]] += 1
                else:
                    Sseen[s[i]] = 1
                if t[i] in Tseen:
                    Tseen[t[i]] += 1
                else:
                    Tseen[t[i]] = 1
            if Sseen == Tseen:
                return True
            
        return False


            
        