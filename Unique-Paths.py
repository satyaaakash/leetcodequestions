class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #top down - memoization solution , time and space : O(m*n)
        # memo ={(0,0):1}

        # def paths(i,j):
        #     if (i,j) in memo:
        #         return memo[(i,j)]
         
                
        #     elif i<0 or j<0 or i==m or j==n:
        #         return 0
        #     else:
        #         val = paths(i,j-1)+paths(i-1,j)
        #         memo[(i,j)] = val
        #         return val

            
        # return paths(m-1,n-1)

        #bottom - up solution , tabulation , space and time : O(m*n)
        dp=[]
        for i in range(m):
            dp.append([0]*n)
        #now full grid was filled with zeros

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
        