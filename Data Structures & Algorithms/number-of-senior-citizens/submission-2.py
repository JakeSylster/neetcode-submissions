#My solution
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior = 0
        
        for pas in details:
            #print(pas[-4:-2])
            if int(pas[-4:-2]) > 60:
                senior += 1
        
        return senior

#Video solution, He gave the same solution but also gave a mathy varient. Let's try recreating it
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for person in details:
            tens = ord(person[11]) - ord("0")
            ones = ord(person[12]) - ord("0")
            age = tens*10 + ones
            if age > 60:
                count += 1
        return count