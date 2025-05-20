class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        #time and space : O(m*n)

        memo = {}

        def dp(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] ==t[j]:
                result = dp(i+1,j+1)+dp(i+1,j)  
                memo[(i,j)]=result
                return result
            else:
                result = dp(i+1,j)
                memo[(i,j)] = result
                return result
        return dp(0,0)      