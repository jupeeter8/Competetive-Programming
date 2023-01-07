from typing import List

# LC 1833
# Problem: Given cost of each ice cream bar and coins, find the maximum number
# of ice cream bars you can buy

# Approach 1:
# Greedy: Sort the cost of ice creams and subtract the cost from coins until
# coins < 0, return the number of ice creams bought


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            if coins - costs[i] < 0:
                return i
            coins -= costs[i]

        return i + 1


def main():

    coins = 7
    cost = [1, 3, 2, 4, 1]

    sol = Solution()
    print(sol.maxIceCream(cost, coins))


main()
