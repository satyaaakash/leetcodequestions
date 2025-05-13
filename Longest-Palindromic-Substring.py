class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0 #variable to store the start location of plaindorme string
        maxlen = 0 #variable to store for length of longest palindrome substring
        
        #define function for algorithm like expand outwards from palindrome to check further 

        def expandAroundCenter(left, right): 
            #declare start and maxlen as nonlocal to use in nested functions
            nonlocal start, maxlen
            while left>=0 and right<len(s) and s[left]==s[right]:
                #check if length of substring is greater than previous substring, if yes then update the values of start and maxlen

                if(right-left+1)>maxlen: 
                    start = left
                    maxlen = right-left+1
                #now update left and right pointers to expand outwards 
                left -=1
                right+=1
        # now to call expand function , traverse each character from string
        for i in range(len(s)):
            expandAroundCenter(i,i) #for odd length
            expandAroundCenter(i,i+1) #for even length
        return s[start:start+maxlen]
        