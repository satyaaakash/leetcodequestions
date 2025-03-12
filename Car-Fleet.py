class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #optimal solution with using hashmap
        hashmap = {position:speed for position,speed in zip(position,speed)}#store key value pairs in hashmap 
        position = sorted(position,reverse=True) #sort them based on positions
        car_fleets = len(position) #assign number of car fleets number to maximum i.e no of positions
        maximum_time =-1 #assign time to -1 

        for i in position:
            time = (target-i)/hashmap[i] #calculate time based on formula
            if time <= maximum_time: # if maximum time is already recorded then will reduce the number of carfleets
                car_fleets -=1
            else:
                maximum_time = time #if not then we will assign the maximum time with time 
        return car_fleets #this will return the no of car fleets 



        #both approaches run in o(nlogn) time complexity but using hashmap will much better time complexity but with stack we can achieve less space complexity. 


        # #another approach to solve this problem using stack 
        # stack = [] #first create a empty stack to store the values of time
        # #here we zip both position and speed to calculate time and will sort them , will start with higher position so that we can backtrack the collision , when both cars collide they will use the minimum speed of both cars and form a car fleet. so we will append only when time is greater than the top of stack and will count the length of stack to find number of car fleets
        # for p,s in sorted(zip(position,speed), reverse = True): 
        #     time = (target - p)/s
        #     if not stack:
        #         stack.append(time)
        #     elif stack[-1]<time:
        #         stack.append(time)
        # return len(stack)
        


