class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:   
        #time and space : O(n)

        intervals.sort(key=lambda interval:interval[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= result[-1][1]:
                result[-1][1]=max(result[-1][1],end)
            else:
                result.append([start,end])
        return result     
        
