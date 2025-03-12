class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #initialize the low and high pointers to start and end of the array 
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = low + (high-low)//2 #find mid of the array
            if nums[mid]==target:
                return mid  #if found target return the index
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return low #if not found then return the low pointer as it will be inserted at that position because loop will terminate at low pointer(low>high)

        