class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = maximum_sum = nums[0]

        for i in range(1,len(nums)):
            if current_sum<0:
                current_sum = nums[i]
            else:
                current_sum+=nums[i]
            if current_sum > maximum_sum:
                maximum_sum = current_sum

            
        
        return maximum_sum



































