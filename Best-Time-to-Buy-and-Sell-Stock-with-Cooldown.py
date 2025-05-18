class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #top-down approach where time and space will be O(n*3)

        dp = {} # (i,buying) is a key and value is max profit and buying is a boolean value 

        def helper(i,buying):
            if i>=len(prices):
                return 0
            
            if (i,buying) in dp:
                return dp[(i,buying)]
            
            cooldown = helper(i+1,buying)
            if buying:
                buy = helper(i+1,not buying) - prices[i]
                dp[(i,buying)] = max(buy,cooldown)
            else:
                sell = helper(i+2,not buying) + prices[i]
                dp[(i,buying)] = max(sell, cooldown)
            return dp[(i,buying)]
        return helper(0,True)


        