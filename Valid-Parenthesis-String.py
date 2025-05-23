class Solution:
    def checkValidString(self, s: str) -> bool:

        #time :O(n), space:O(1)

        low,high = 0,0
        
        for c in s:
            if c=="(":
                low+=1
                high+=1
            elif c==")":
                low-=1
                high-=1
            
            elif c=="*":
                low-=1
                high+=1
            
            if high<0:
                return False
            
            
            low = max(low,0)
        return low==0
        