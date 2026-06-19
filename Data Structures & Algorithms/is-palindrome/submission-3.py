# Using Loop
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for char in s:
            if char.isalnum():
                ns += char.lower()
        
        return ns == ns[::-1]
        
        # if ns == ns[::-1]:
        #     return True
        # else:
        #     return False
        

#Using pointers and if-else ladder
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left].lower() != s[right].lower():
                        return False
                    else:
                        left += 1
                        right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return True

