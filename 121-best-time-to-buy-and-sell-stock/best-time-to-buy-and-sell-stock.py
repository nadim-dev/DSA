class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start=0
        j=1
        profit=0
        while(j<len(prices)):
            amountEarn=prices[j]-prices[start]
            if(amountEarn > profit):
                profit=amountEarn
            if(amountEarn < 0):
                start=j
            j=j+1
        return profit