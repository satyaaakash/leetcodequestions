import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #first we need to find the frequencies of tasks and we use maxHeap here to solve because it can give the max freq element in logn .

        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]

        #initiate heapify to make it maxHeap
        heapq.heapify(maxHeap)
        #initialize queue to store the updated count and time need to be wait for again to taks need to be completed 

        queue = deque()
        #intialize time =0
        time =0

        #now run loop till maxHeap or queue becomes empty

        while maxHeap or queue :
            #now increase the time whenever loop initiated i.e it traverses each value in maxHeap or queue
            time +=1

            #now check if maxHeap exists then pop element from it the maximum and update its count 
            if maxHeap:
                cnt=1+heapq.heappop(maxHeap)
                #if cnt not zero then append them into queue and wait for the time to be matched 
                if cnt:
                    queue.append([cnt,time+n])
            #when the time matches with queue stored time then need to push again into maxHeap
            if queue and queue[0][1]==time:
                heapq.heappush(maxHeap,queue.popleft()[0])
        return time