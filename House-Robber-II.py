class Solution:
    def rob(self, nums: List[int]) -> int:
        #top down approach memoization , time and space: O(n)
        # n =len(nums)
        # if n==1:
        #     return nums[0]
        

        # def helper(arr):
        #     m =len(arr)
        #     if m==0:
        #         return 0
        #     if m==1:
        #         return arr[0]
        #     memo = {0:arr[0], 1:max(arr[0],arr[1])}

        #     def top(i):
        #         if i in memo:
        #             return memo[i]
        #         else:
        #             memo[i] = max(top(i-2)+arr[i], top(i-1))
        #             return memo[i]
        #     return top(m-1)
        # return max(helper(nums[:-1]),helper(nums[1:]))

        #bottom up approach , time and space :O(n)

        # n = len(nums)
        # if n==1:
        #     return nums[0]
        
        # def helper(arr):
        #     m =len(arr)
        #     if m==0:
        #         return 0
        #     if m==1:
        #         return arr[0]
            
        #     dp = [0]*m
        #     dp[0] = arr[0]
        #     dp[1] = max(arr[0],arr[1])

        #     for i in range(2,m):
        #         dp[i] = max(dp[i-2]+arr[i],dp[i-1])
        #     return dp[m-1]
        # return max(helper(nums[:-1]),helper(nums[1:]))

        #bottom up approach with constant space , time :O(n), space:O(1)

        n =len(nums)
        if n==1:
            return nums[0]
        
        def helper(arr):
            m = len(arr)
            if m==0:
                return 0
            if m==1:
                return arr[0]
            
            prev, curr = arr[0],max(arr[0],arr[1])

            for i in range(2,m):
                prev, curr = curr, max(arr[i]+prev, curr)
            return curr
        return max(helper(nums[:-1]), helper(nums[1:]))

