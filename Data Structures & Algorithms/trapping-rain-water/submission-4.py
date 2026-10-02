class Solution:
    def trap(self, height: List[int]) -> int:
        # result = 0
        # counter = 0
        # indexI = 0
        # for indexJ in range(indexI+1,len(height)):
        #     if height[indexJ] >=  height[indexI]:
        #         result += counter
        #         counter = 0
        #         indexI = indexJ
        #     elif indexJ < indexI and indexJ == len(list) - 1:
        #         counter = 0
        #     else:
        #         counter += height[indexI] - height[indexJ]
        # return int(result)

        # Video non-efficient Solution
        # indexI = 0
        # indexJ = 0
        # waterTrapped = 0
        # for indexI in range(1,len(height)-1):
        #     leftMax = max(height[0:indexI])
        #     rightMax = max(height[indexI+1:])
        #     minLength = min(leftMax,rightMax)
        #     if minLength < 0:
        #         minLength = 0
        #     if minLength - height[indexI] < 0:
        #         continue
        #     waterTrapped += minLength - height[indexI]
            
        # return waterTrapped

        #Video efficient solution
        i,j = 0,len(height) - 1
        maxL,maxR = height[i],height[j]
        waterTrapped = 0
        while i<j:
            if maxL < maxR:
                i += 1
                maxL = max(maxL,height[i])
                waterTrapped += maxL - height[i]
            else:
                j -= 1
                maxR = max([maxR,height[j]])
                waterTrapped += maxR - height[j]
        return waterTrapped
