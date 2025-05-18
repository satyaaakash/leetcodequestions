class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom - up approach , time : O(amount *coins), space : O(amount)
        
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i],1+dp[i-coin])
        if dp[amount]!= (amount+1):
            return dp[amount]
        else:
            return -1
        
        #top-down approach , time : O(amount*coins), space : O(amount)

        # memo = {}

        # def helper(amount):
        #     if amount ==0 :
        #         return 0
        #     if amount in memo:
        #         return memo[amount]
            
        #     result = float('inf')

        #     for coin in coins:
        #         if amount - coin >=0:
        #             result = min(result, 1+helper(amount-coin))
        #     memo[amount] = result
        #     return result 
        # mincoins = helper(amount)
        # return mincoins if mincoins!=float('inf') else -1
            