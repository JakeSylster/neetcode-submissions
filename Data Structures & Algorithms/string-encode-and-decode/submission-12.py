class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return str(strs)
        encodedString = "..".join(strs)
        return encodedString
    

    def decode(self, s: str) -> List[str]:
        decodedList = []
        if s == "[]":
            return decodedList
        if s == "[""]" or s =="['']":
            decodedList = [""]
            return decodedList
        decodedList = s.split("..")
        # if not decodedList:
        #     return decodedList
        return decodedList

# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         cipher = ""
#         for string in strs:
#             for letter in string:
#                 cipher += str(ord(letter))
#                 cipher += "$"
#             if string == strs[-1]:
#                 break
#             cipher += "#"
#         print(cipher)
#         return cipher 

#     def decode(self, s: str) -> List[str]:
#         words = []
#         asciiWords = list(s.split("#"))
#         print(asciiWords)
#         for string in asciiWords:
#             listOfLetters = []
#             listOfLetters = list(string.split("$")[:-1])
#             word = ""
#             for letter in listOfLetters:
#                 word += chr(int(letter))
#             words.append(word)
#         return words