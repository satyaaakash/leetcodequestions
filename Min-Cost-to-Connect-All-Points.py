class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:


        #minimum spanning tree (prims approach) time: o(n^2 logn)

        n = len(points)
        total_cost =0
        visited = set()
        min_heap = [(0,0)]

        def manhattan(i,j):
            return abs(points[i][0]-points[j][0])+ abs(points[i][1]-points[j][1])
        
        while len(visited)<n:
            cost, point_index = heapq.heappop(min_heap)

            if point_index in visited:
                continue
            
            visited.add(point_index)
            total_cost+=cost

            for index in range(n):
                if index not in visited:
                    heapq.heappush(min_heap, (manhattan(point_index,index),index))
        return total_cost

        