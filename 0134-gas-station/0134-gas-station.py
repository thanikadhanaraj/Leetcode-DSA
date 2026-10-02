class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        total_sum = 0
        current_sum = 0
        start_index = 0

        for i in range(len(gas)):

            total_sum += gas[i] - cost[i]
            current_sum += gas[i] - cost[i]

            if current_sum < 0:
                current_sum = 0
                start_index = i + 1

        if total_sum >= 0:
            return start_index
        else:
            return -1