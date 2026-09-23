class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #BrutrForce
        # maxArea = 0
        # for indexI,breadth in enumerate(heights):
        #     for indexJ in range(indexI+1,len(heights)):
        #         b = min(breadth,heights[indexJ])
        #         length = indexJ-indexI
        #         area = length * b
        #     maxArea = max(maxArea,area)
        # return maxArea

        #Efficient Solution
        maxArea = 0
        indexI = 0
        indexJ = len(heights) - 1 

        while indexI != indexJ:
            breadth = min(heights[indexI],heights[indexJ])
            length = indexJ-indexI
            area = length * breadth

            maxArea = max(maxArea,area)

            if heights[indexI] <= heights[indexJ]:
                indexI += 1
            else:
                indexJ -= 1
        return maxArea



            

        
        