class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize pointers in binary search
        low, high = 0,len(nums)-1
        while low<=high:
            #find mid
            mid = low+(high-low)//2
            if nums[mid] == target:
                return mid
            #check the low element is lower than mid 
            if nums[low]<=nums[mid]:
                #then check both possibilities of going to righ side of list 
                if nums[mid]<target or nums[low]>target:
                    low = mid+1
                else:
                    high =mid -1
            else:
                #check both possibilities of going left side
                if nums[mid]>target or target>nums[high]:
                    high = mid -1
                else:
                    low =mid+1
        return -1

                    
        