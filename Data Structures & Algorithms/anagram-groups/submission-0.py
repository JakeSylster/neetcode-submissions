class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for string in strs:
            numString = [0] * 26
            
            for char in string:
                numString[ord(char)-ord("a")] += 1
            
            seen[tuple(numString)].append(string)
        
        return list(seen.values())


        
        