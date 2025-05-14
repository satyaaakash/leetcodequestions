class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom - up approach , time : O(amount *coins), space : O(amount)
        coins.sort()
        dp = [0]*(amount+1)

        for i in range(1,amount+1):
            minimum = float('inf')
            for coin in coins:
                diff = i- coin
                if diff <0:
                    break
                minimum = min(minimum,dp[diff]+1)
            dp[i] = minimum
        if dp[amount]<float('inf'):
            return dp[amount] 
        else:
            return -1       

        #top-down approach , time and space as bottom up , but btoom up is faster than this
        # coins.sort()
        # memo ={0:0}

        # def dfs(amt):

        #     minimum = float('inf')

        #     if amt in memo:
        #         return memo[amt]
            
        #     for coin in coins :
        #         diff = amt - coin
        #         if diff<0:
        #             break
        #         minimum = min(minimum,dfs(diff)+1)
        #     memo[amt] = minimum
        #     return minimum
        # if dfs(amount)<float('inf'):
        #     return dfs(amount)
        # else:
        #     return -1