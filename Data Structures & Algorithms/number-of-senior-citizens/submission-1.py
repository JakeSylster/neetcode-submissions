#My solution
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior = 0
        
        for pas in details:
            #print(pas[-4:-2])
            if int(pas[-4:-2]) > 60:
                senior += 1
        
        return senior