class MedianFinder:

    

    def __init__(self):
        #initialize two heaps for two halfs , where maxheap will have the smaller numbers and min heap will have the larger number , both heap roots will be the median
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        #first check if maxheap is not empty or if the num is smaller than the current root of max heap then it should be pushed to maxheap with -num or else to minheap
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap,-num)
        else:
            heapq.heappush(self.minHeap,num)
        #after adding check whether both have equal numbers in both heaps , if the length of array is odd then in min heap there will be one extra number compared to minheap and root of max heap would be the median , other than that you need transfer to make that condition (equal lengths in both heaps)
        if len(self.maxHeap) > len(self.minHeap)+1:
            heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        elif len(self.maxHeap)<len(self.minHeap):
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap)) 
    
        

    def findMedian(self) -> float:
        #if both the heaps lengths are equal then it is even , so find the average of two roots 
        if len(self.minHeap)==len(self.maxHeap):
            return float((-self.maxHeap[0]+self.minHeap[0])/2)
        #else it is odd, so return the root of max heap
        else:
            return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()