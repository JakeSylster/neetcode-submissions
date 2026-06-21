#Using loops
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newarr = [0] * len(arr)
        for i in range(len(arr)):
            greatest = 0
            for j in range(i+1,len(arr)):
                greatest = max(arr[j],greatest)
            newarr[i] = greatest
        newarr[-1] = -1
        return newarr

#Using logic provided by video
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lastvalue = -1

        for i in range(len(arr)-1,-1,-1):
            maxvalue = max(lastvalue, arr[i])
            arr[i] = lastvalue
            lastvalue = maxvalue
        return arr



