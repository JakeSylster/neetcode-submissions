#Using loops. Own solution
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1 = []
        list2 = []

        for i in nums1:
            if i not in nums2 and i not in list1:
                list1.append(i)
        for j in nums2:
            if j not in nums1 and j not in list2:
                list2.append(j)
                
        return [list1,list2]
        
#Video solution, Wow the video solution was the same except for insitalize as a set and convert it into a list at the end
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result1 , result2 = set(), set()

        for i in nums1:
            if i not in nums2:
                result1.add(i)
        for j in nums2:
            if j not in nums1:
                result2.add(j)

        return[list(result1),list(result2)]


