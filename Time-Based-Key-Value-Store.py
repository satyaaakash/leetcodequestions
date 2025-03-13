class TimeMap:

    def __init__(self):
        #initialize hashmap to store key value pairs
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #define set function with appending value and timestamp to appropriate key 
        if key not in self.hashmap:
            self.hashmap[key]=[]
        self.hashmap[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        #to define get function with using binary search
        #first reterive value and time stamp from hashmap 
        values = self.hashmap.get(key,[])
        result =""
        low = 0
        high = len(values)-1

        while low<=high:
            mid = low+(high-low)//2 #calculate mid

            if values[mid][1]<=timestamp: #check if timestamp at mid is lower than given mid then move low to mid +1 to check required time stamp
                result = values[mid][0] #store the previous timestamp in result. 
                low = mid+1
            else:
                high = mid-1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)