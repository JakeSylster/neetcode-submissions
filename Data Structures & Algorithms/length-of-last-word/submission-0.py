class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        listofwords = []
        listofwords = s.split()
        return (len(listofwords[-1]))

        