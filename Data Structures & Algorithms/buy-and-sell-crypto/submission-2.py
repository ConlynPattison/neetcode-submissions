class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return max profit (buy day - sell day)
        # no transactions is valid -> return 0

        """
        lowest_seen <- 101 # places beyond constraint
        max_profit <- 0

        track these in iteration:
            if new low is found, change lowest seen and continue (can't be best day)
            otherwise, check for new best profit
        
        return best profit (could be zero)
        """
        
        lowest_seen = 101
        max_profit = 0

        for price in prices:
            if price < lowest_seen:
                lowest_seen = price
                continue
            max_profit = max(max_profit, price - lowest_seen)
        
        return max_profit