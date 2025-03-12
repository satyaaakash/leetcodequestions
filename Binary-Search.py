class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize low and high in this conditions
        low = 0
        high = len(nums) - 1
        #now find mid 

        while low<=high:
            mid = low+(high-low)//2

            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                high = mid -1
            else:
                low = mid+1
        return -1
        