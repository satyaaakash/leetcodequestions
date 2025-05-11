class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        #modifies bfs (dijkstras with stops constraint)

        #initialize adjaceny list of graph

        graph = defaultdict(list)

        for source, destination, price in flights:
            graph[source].append((destination,price))
        
        min_heap =[(0,src,0)] #cost,city,stops

        best_price ={}

        while min_heap:
            cost, city, stops = heapq.heappop(min_heap)

            if city == dst:
                return cost

            if (city,stops) in best_price and best_price[(city,stops)]<=cost:
                continue
            best_price[(city,stops)] = cost
            
            if stops <= k:
                for nei, nei_price in graph[city]:
                    heapq.heappush(min_heap,(cost+nei_price, nei, stops+1))
        return -1
        