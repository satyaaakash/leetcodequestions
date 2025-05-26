class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #time and space: O(n)
        result = []
        Inserted = False

        for interval in intervals:
            # new interval will be inserted completely after the existing intervals
            if interval[1]<newInterval[0]:
                result.append(interval)
            #new interval will be inserted completely before the existing intervals
            elif interval[0]>newInterval[1]:
                if not Inserted:
                    result.append(newInterval)
                    Inserted = True
                result.append(interval)
            #if not both the cases i.e overlapping , so merge both the intervals and produce[min,max]
            else:
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] =max(interval[1],newInterval[1])
        if not Inserted:
            result.append(newInterval)
        return result