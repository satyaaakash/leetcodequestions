class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        #create a graph which adjacency list 
        graph = defaultdict(list)
        # i use default dict here to create a adjacency list , where if you access a key that doesnot exist, it automatically creates it with a default empty list

        for u,v,w in times:
            graph[u].append((v,w)) #here u i.e source node acts as key and v i.e target node and w which is distance/time that needs to travel acts as value 
        
        min_times = {}  # initiaLIZES dictionary to store the minimum
        min_heap = [(0,k)] 
        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in min_times:
                continue
            min_times[node] = time

            for neighbor, neighbor_time in graph[node]:
                if neighbor not in min_times:
                    heapq.heappush(min_heap,(time+neighbor_time,neighbor))
        if len(min_times)==n:
            return max(min_times.values())
        return -1
            
            
        