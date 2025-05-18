class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #time and space : O(n*amount), n-> len(coins)

        memo ={}
        
        def helper(i,n):
            if (i,n) in memo:
                return memo[(i,n)]
            if i>=len(coins) or n<=0:
                return 1 if n==0 else 0
            count = helper(i,n-coins[i])+helper(i+1,n)
            memo[(i,n)] = count
            return count
        return helper(0,amount)
        