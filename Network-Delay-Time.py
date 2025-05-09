class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        #create a graph which adjacency list 
        graph = defaultdict(list)
        # i use default dict here to create a adjacency list , where if you access a key that doesnot exist, it automatically creates it with a default empty list

        for u,v,w in times:
            graph[u].append((v,w)) #here u i.e source node acts as key and v i.e target node and w which is distance/time that needs to travel acts as value 
        
        min_times = {}  # initializes dictionary to store the minimum
        min_heap = [(0,k)] #initialize min heaop with 0 as distance/time and k as given node 
        while min_heap: #till min_heap gets empty
            time, node = heapq.heappop(min_heap) # pop out the shortest distance in the heap

            # if node was alrready min_heap then continue , if not then assign time to that node in hashmap to permenanetly store that the value(time/weright) will be minimum for that node 

            if node in min_times: 
                continue
            min_times[node] = time

            for neighbor, neighbor_time in graph[node]:  #traverser through all available neighbors to thast node
                if neighbor not in min_times: # if neighbor was not in hashmap 
                    heapq.heappush(min_heap,(time+neighbor_time,neighbor)) #then push that time + neighbor time with that neighbor node to min_heap 
        if len(min_times)==n:
            return max(min_times.values())
        return -1
            
            
        