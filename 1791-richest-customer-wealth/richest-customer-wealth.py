class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=0
        for account in accounts:
            row_sum=0
            for cash in account:
                row_sum+=cash
            
            if(wealth < row_sum):
                wealth=row_sum
        return wealth