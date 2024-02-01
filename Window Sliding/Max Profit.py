class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Question Link:
            Intuition:It iterates through the prices, updating min_price to the minimum of the current price and min_price.
            For each price, it calculates the profit by subtracting the minimum price from the current price.
            It updates max_profit to the maximum of the current profit and max_profit.
            After iterating through all prices, it returns the maximum profit obtained.
        """
        # Initialize variables to track the minimum price and maximum profit
        min_price = prices[0]
        max_profit = 0

        # Iterate through the prices
        for price in prices:
            # Update the minimum price seen so far
            min_price = min(min_price, price)
            # Update the maximum profit if selling at the current price yields a higher profit
            max_profit = max(max_profit, price - min_price)

        # Return the maximum profit
        return max_profit