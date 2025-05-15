class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #bottom up solution , time:O(n^2), space: O(n)
        n = len(nums)

        dp = [1]*n

        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)
        