class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #to find the peak element, we need to traverse till low<high , because when low=high case will be at either last element in the array where the next mid+1 will be not there and we can consider that as peak , so we return low 
        low = 0
        high = len(nums)-1
        while low<high:
            mid = low+(high-low)//2
            if nums[mid]<=nums[mid+1]:#if right neighbour is large then to find peak low will move to right side
                low=mid+1
            else:
                high = mid #when it exucted we know that there is no chance for the right neighbour to be peak , so we changed mid to left side to check another cases
        return low 



        