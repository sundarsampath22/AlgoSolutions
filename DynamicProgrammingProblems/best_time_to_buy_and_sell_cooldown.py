#Recursion/memoization 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #cache[i, x] = max profit if starting on day i and holding x amount of stock
        cache = {}
        def dfs(currentDay, prices, holdingStock):
            nonlocal cache
            if currentDay >= len(prices):
                return 0
            if (currentDay, holdingStock) in cache:
                return cache[(currentDay, holdingStock)]
            currentPriceOfStock = prices[currentDay]
            if holdingStock == None:
                #max_profit I can make if I buy right now vs if I buy later
                buy_now = dfs(currentDay + 1, prices, currentPriceOfStock)
                buy_later = dfs(currentDay + 1, prices, holdingStock)
                cache[(currentDay, holdingStock)] = max(buy_now, buy_later)
                return cache[(currentDay, holdingStock)]
            else:
                #The max profit if I sell what I have right now and continue two days later
                sell_now = dfs(currentDay + 2, prices, None) + (currentPriceOfStock - holdingStock)
                #The max profit if I don't sell now
                sell_later = dfs(currentDay + 1, prices, holdingStock)
                cache[(currentDay, holdingStock)] = max(sell_now, sell_later)
                return cache[(currentDay, holdingStock)]
        return dfs(0, prices, None)

            
            