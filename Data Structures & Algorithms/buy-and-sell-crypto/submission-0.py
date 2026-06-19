#Using loops
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxsell = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] > prices[i]:
                    diff = prices[j] - prices[i]
                    if diff>maxsell:
                        maxsell = diff
        return maxsell        
                
#Using pointers
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxprofit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxprofit = max(profit,maxprofit)
            else:
                l = r
            r += 1
        return maxprofit
