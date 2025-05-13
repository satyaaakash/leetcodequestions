class Solution:
    def countSubstrings(self, s: str) -> int:
        #in the same way you solve longest plaindromic substring , just remove the length nd calculate count
        count = 0

        #define a function for expandAroundCenter , like you expand outwards to find paindrome substring
        def expandAroundCenter(left, right):
            nonlocal count

            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        #now call expand function for odd length and even length, where in both calls,all the possibilities wiull be covered

        for i in range(len(s)):
            expandAroundCenter(i,i) #odd length 
            expandAroundCenter(i,i+1)
        return count

        
        