class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        
        
        indegree =[0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1

        queue = deque()

        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        if len(order) == numCourses:
            return order
        else:
            return []