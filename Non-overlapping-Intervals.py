class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #time :O(nlogn), space:O(1)

        intervals.sort(key=lambda interval:interval[1])
        result = intervals[0][1]
        count =1

        for start,end in intervals[1:]:
            if start>=result:
                result = end 
            
                count+=1
                
        return len(intervals)-count
        