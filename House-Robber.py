class Solution:
    def rob(self, nums: List[int]) -> int:
        #top dowm approcach memoization , time : O(n), space: O(n)

        # n = len(nums)

        # if n ==1:
        #     return nums[0]
        # if n==2:
        #     return max(nums[0], nums[1])
        
        # memo ={0:nums[0], 1:max(nums[0],nums[1])}

        # def helper(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = max(helper(i-2)+nums[i],helper(i-1))
        #         return memo[i]
        # return helper(n-1)

        #bottom-up approach tabulation , time, space : o(n)

        # n=len(nums)
        # if n==1:
        #     return nums[0]
        # if n==2:
        #     return max(nums[0],nums[1])
        # dp = [0]*n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1])

        # for i in range(2,n):
        #     dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        # return dp[n-1]

        #bottom up approach with constant space , time :O(n), space: O(1)

        n = len(nums)


        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        
        prev, curr = nums[0],max(nums[0],nums[1])

        for i in range(2,n):
            prev, curr = curr, max(nums[i]+prev, curr)
        return curr