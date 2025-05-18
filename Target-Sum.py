class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #time and space : O(n*total_sum)
        memo = {}

        def dp(i,n):
            if (i,n) in memo:
                return memo[(i,n)]
            
            #base case:
            if i==len(nums):
                return 1 if n==target else 0
            
            count =dp(i+1,n+nums[i])+dp(i+1,n-nums[i])
            memo[(i,n)] = count
            return count 
        return dp(0,0)
        