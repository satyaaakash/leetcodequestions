class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src],dst)
        result =[]

        def dfs(source):
            while graph[source]:
                dfs(heapq.heappop(graph[source]))
            result.append(source)
        
        dfs("JFK")
        return result[::-1]



        # graph = defaultdict(list)

        # for source, destination in sorted(tickets, reverse = True):
        #     graph[source].append(destination)
        
        # stack = ["JFK"]
        # iternary = []

        # while stack:
        #     current = stack[-1]

        #     if not graph[current]:
        #         iternary.append(stack.pop())
        #     else:
        #         next_city = graph[current].pop()
        #         stack.append(next_city)

        # return iternary[::-1]


        #time complexity same for both approaches (O(ElogE)), space complexity is bettern in sorted reverse approach