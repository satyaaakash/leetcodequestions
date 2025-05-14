class Solution:
    def numDecodings(self, s: str) -> int:
        n =len(s)

        if n ==0 or s[0]=="0":
            return 0
        
        dp = [0]*(n+1)

        dp[0], dp[1] =1,1

        for i in range(2,n+1):
            one_digit = int(s[i-1])
            two_digit = int(s[i-2:i])

            if 1<=one_digit<=9:
                dp[i]+=dp[i-1]
            if 10<=two_digit<=26:
                dp[i]+=dp[i-2]
        return dp[n]      
        

        # n= len(s)
        # if n==0 or s[0]=="0":
        #     return 0
        
        # prev, curr =1,1

        # for i in range(2,n+1):
        #     one_digit = int(s[i-1])
        #     two_digit = int(s[i-2:i])

        #     count = 0

        #     if 1<=one_digit<=9:
        #         count+=curr
        #     if 10<=two_digit<=26:
        #         count+=prev
            
        #     prev,curr = curr, count
        # return curr

        # n= len(s)

        
        # memo ={}
        # def dfs(i):
        #     if i ==n:
        #         return 1
        #     if s[i]=="0":
        #         return 0
            
        #     if i in memo :
        #         return memo[i]
            
        #     count = dfs(i+1)

        #     if i+1<n and 10<=int(s[i:i+2])<=26:
        #         count+=dfs(i+2)
        #     memo[i]=count
        #     return count
        # return dfs(0)
