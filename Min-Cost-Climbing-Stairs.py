class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        #top-down (memoization approach) time , space : O(n)

        # n = len(cost)

        # memo ={0:0, 1:0}

        # def mincost(i):
        #     if i in memo:
        #         return memo[i]
            
        #     else:
        #         memo[i] = min(cost[i-2]+mincost(i-2), cost[i-1]+mincost(i-1))
        #         return memo[i]
        # return mincost(n)
        
        #bottom -up (tabulation approach) time,space : O(n)
        # n=len(cost)

        # dp = [0]*(n+1)
        # dp[0], dp[1] = 0,0

        # for i in range(2,n+1):
        #     dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        # return dp[n]

        # msot efficent with same approach with constant space

        n= len(cost)

        prev, curr = 0,0

        for i in range(2, n+1):
            prev, curr = curr, min(cost[i-2]+prev, cost[i-1]+curr)
        return curr