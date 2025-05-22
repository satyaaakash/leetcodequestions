class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #greedy approach time:O(n), space:O(1)
        if sum(gas)<sum(cost):
            return -1
        total_tank = 0
        start_station = 0

        for i in range(len(gas)):
            total_tank += gas[i]-cost[i]

            if total_tank <0:
                total_tank = 0
                start_station =i+1
        return start_station
        