class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #create a stack to check the temperatures
        stack = []
        result = [0]*len(temperatures) #create result array with zeroes , so that the last elements and if there are no higher temperatures greater than already recorded temperatures will return 0

#now the loop iterates through input list with enumerate which will have index and the value 
        for index,temperature in enumerate(temperatures): 
            #it will check if stack was not empty and whenever the temperature from input list was greater than the top of stack , then it will pop the element and also assign the number of days in result list.  here we use tuple to store the data of temp and index in stack 
            while stack and stack[-1][0]<temperature:
                stack_temperature,stack_index = stack.pop() 
                result[stack_index] = index -stack_index
            stack.append((temperature,index))
        return result
#we used monotonic decreased stack with timecomplex:o(n) and space:o(n)