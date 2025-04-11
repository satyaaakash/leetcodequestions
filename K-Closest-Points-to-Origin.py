class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        #will use Maxheap for optimal space complexity:

        maxHeap = []

        for x,y in points:
            distance = -(x**2+y**2)
            heapq.heappush(maxHeap,[distance,x,y])
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        result = []
        for distance,x,y in maxHeap:
            result.append([x,y])
        return result


        #using min heap results in space complexity of O(n)

        # minHeap = []

        # for x,y in points:
        #     distance = x**2+y**2
        #     minHeap.append([distance,x,y])
        # heapq.heapify(minHeap)

        # result = []

        # while k>0:
        #     distance,x,y = heapq.heappop(minHeap)
        #     result.append([x,y])
        #     k-=1
        # return result
        