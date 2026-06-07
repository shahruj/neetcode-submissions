class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        
        maxprofit = 0
        for right in range(0,len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                maxprofit = max(maxprofit,prices[right]-prices[left])
        
        return maxprofit

            

        