class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #we need to use two binary searches here to find first occurence and last occurence 

        #when we found our first occurence will move our high to mid -1 for previous occurences
        def firstoccurence(nums,target):
            low =0
            high = len(nums)-1
            first = -1

            while low <=high:
                mid = low+(high-low)//2
                if nums[mid]==target:
                    first = mid
                    high = mid-1
                elif nums[mid]>target:
                    high =mid-1
                else:
                    low = mid+1
            return first
        #to find second occurence will move our low to mid+1 for next occurences
        def secondoccurence(nums,target):
            low =0
            high =len(nums)-1
            second =-1
            while low<=high:
                mid = low+ (high-low)//2
                if nums[mid]==target:
                    second = mid 
                    low =mid +1
                elif nums[mid]>target:
                    high = mid-1
                else:
                    low =mid+1
            return second
        
        first = firstoccurence(nums,target)
        second = secondoccurence(nums,target)
        return [first,second]
        