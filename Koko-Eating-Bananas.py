class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #initialize low and high here we tke the max pile as high for calculating the minimum speed k rate and low as 1 because low could be 1 hour atleast 
        low=1
        high = max(piles)
        result = high 
        #iterate binarysearch and find mid
        while low<=high:
            mid =low+(high-low)//2
            #now calculate total time taken with that mid
            total_time=0
            for p in piles:
                total_time+=math.ceil(p/mid)
            #compare with given h if it is more than given h then move low to mid+1 , so that time will be less , or given h is more than total time then move right to mid-1 and also store result 
            if total_time<=h:
                result = min(result,mid)
                high = mid -1
            else:
                low = mid+1
        return result
        