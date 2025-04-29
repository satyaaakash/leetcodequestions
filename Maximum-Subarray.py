class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        total =0

        for i in range(len(nums)):
            if total <0:
                total =0
            total+=nums[i]
            result = max(result,total)
        return result
        