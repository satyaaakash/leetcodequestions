import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if len(self.minHeap)<self.k or self.minHeap[0]<val:
            heapq.heappush(self.minHeap,val)
            if len(self.minHeap)>self.k:
                heapq.heappop(self.minHeap)

        return self.minHeap[0]
       

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)