class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #time complexity: O((n+m)logn), space:O(n+m), n= len(intervals), m=len(queries)

        intervals.sort(key=lambda interval:interval[0])#sort by start time 

        result =[-1]*len(queries)

        sorted_queries = []

        for i,q in enumerate(queries):
            sorted_queries.append((q,i))
        sorted_queries = sorted(sorted_queries)

        min_heap = []
        i=0

        for query, index in sorted_queries:
            while i<len(intervals) and intervals[i][0]<=query:
                start,end = intervals[i]
                if end>=query:
                    heapq.heappush(min_heap,(end-start+1,end))
                i+=1
            
            while min_heap and min_heap[0][1]<query:
                heapq.heappop(min_heap)
            
            if min_heap:
                result[index]=min_heap[0][0]
            
        return result

        