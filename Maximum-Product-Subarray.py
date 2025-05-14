class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curr_max, curr_min, result = nums[0],nums[0],nums[0]

        for i in range(1,len(nums)):
            num = nums[i]
            if num<0:
                curr_max,curr_min = curr_min,curr_max
            

            curr_max = max(num,curr_max*num)
            curr_min = min(num,curr_min*num)
            result = max(result,curr_max)
        return result

        