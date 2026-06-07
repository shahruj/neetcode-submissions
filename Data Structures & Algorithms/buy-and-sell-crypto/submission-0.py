class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        
        maxprofit = 0
        for right in range(0,len(prices)):
            while prices[left] > prices[right]:
                left+=1
            maxprofit = max(maxprofit,prices[right]-prices[left])
        
        return maxprofit

            

        