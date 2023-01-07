from typing import List

# LC 134

# Problem: Given a circular array of gas stations and the cost to travel from
# one station to the next, find the starting gas station that can complete the
# circuit

# Approach 1 - Greedy
# Question maintains there is only one unique solution, create a difference
# array cost[i] - gas[i], if the sum of difference array is negative, there is
# no solutionif sum(diff) >= 0, there is a solution, start from the first
# station, and keep track of starting station, if at any point total gas
# becomes negative, starting station is not the solution, set start = start + 1
# and gas = 0. # continue until the end of the array, since we are garunteed a
# solution, the starting station that did not end up being negative will be our
# solution, Time O(n), Space O(1)


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diff) < 0:
            return -1

        start = 0
        gasInTank = 0

        for i in range(len(diff)):
            gasInTank += diff[i]
            if gasInTank < 0:
                start = i + 1
                gasInTank = 0
        return start


def main():
    sol = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    print(sol.canCompleteCircuit(gas, cost))


main()
