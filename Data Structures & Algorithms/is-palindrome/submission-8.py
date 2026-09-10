class Solution:
    def isPalindrome(self, s: str) -> bool:
        fake=""
        for ch in s:
            if 97 <= ord(ch) <= 122 or 65 <= ord(ch) <= 90 or 48<= ord(ch) <= 57:
                fake+=ch
                print(fake)
        fake=fake.lower()
        if fake==fake[::-1]:
            return True
        return False