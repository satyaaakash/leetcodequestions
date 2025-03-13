class Solution:
    def findMin(self, nums: List[int]) -> int:
        #initialize pointers in binarysearch
        low =0
        high = len(nums)-1
        result = nums[high] #we can assign any number to it 
        while low<=high:
            mid = low+(high-low)//2
            result = min(result,nums[mid]) #checks the minimum and stores it to result
            if nums[mid]>nums[high]: #if nums[high] is less than the mid then smaller numbers are positioned at right side of mid, so i want to move low to mid+1 
                low = mid+1
            else:
                high = mid -1
        return result
        
        