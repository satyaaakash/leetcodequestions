class Twitter:

    def __init__(self):
        #first initialize tweets for the user to store , they can have multiple tweets so will create a list of defaultdict (because to map users to that list of thewir own tweets )
        self.tweets = defaultdict(list)
        #same way also create a set to store unique followers for user
        self.followers = defaultdict(set)
        #initialize timestamp for ordering and to extract most recent 10 
        self.timestamp=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #whenever user posts a tweet we need to append tweetId that to list along with time stamp 
        self.tweets[userId].append((self.timestamp,tweetId))
        #and also increase the time stamp whenever user posts a tweet
        self.timestamp +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #create a min heap to not sort every time and get the result for most recent 
        minHeap =[]

        #now check if user has any tweets and add them to heap

        if userId in self.tweets:
            #extract each tweet and push to heap 
            for tweet in self.tweets[userId]:
                heapq.heappush(minHeap,tweet)
                #if heap length has crossed 10 , then pop it so that oldest tweet will be removed
                if len(minHeap)>10:
                    heapq.heappop(minHeap)
            
        #now check if user is following had any tweets and add them to heap , fetch all tpogetger top 10 tweets to be displayed on timeline
        if userId in self.followers:
            #if user is in followers list then fectch the followers of that user
            for followee in self.followers[userId]:
                #check if that followee had any tweets
                if followee in self.tweets:
                    #now extract each tweet and append to heap 
                    for tweet in self.tweets[followee]:
                        heapq.heappush(minHeap,tweet)
                        if len(minHeap)>10:
                            heapq.heappop(minHeap)
        #create empty list to display top 10 tweets 
        result = []
        while minHeap:
            #pop all the 10 tweets from final heap based on most recent 
            result .append(heapq.heappop(minHeap)[1])
        #as we used minHeap so latest will be last one so will reverse the list so that will start from recent one 
        result.reverse()
        #then return result
        return result
            

    def follow(self, followerId: int, followeeId: int) -> None:
        #if user follows someone then we need to add that follower to set 
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #if user is following someone then remove from that set 
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)