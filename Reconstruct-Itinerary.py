class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)

        for source, destination in sorted(tickets, reverse = True):
            graph[source].append(destination)
        
        stack = ["JFK"]
        iternary = []

        while stack:
            current = stack[-1]

            if not graph[current]:
                iternary.append(stack.pop())
            else:
                next_city = graph[current].pop()
                stack.append(next_city)

        return iternary[::-1]


        