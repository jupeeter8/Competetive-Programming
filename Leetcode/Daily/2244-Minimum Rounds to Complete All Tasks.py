# 2244. Minimum Rounds to complete All Tasks
# Given an array of tasks find the minimum number of rounds to complete all
# tasks. You can choose to complete either 2 or 3 of the same task in a round.
# Return the number of rounds or -1 if it is not possible to complete the task

# Approach 1: DP using meoization.
# Reccursively calculate the number of rounds for each choice of 2 and 3
# Store the minimum of the two in memo

# Approach 2: Greedy, If anything is greater than 1, ther exists a combination
# of 2 and 3 in a way that adds up to the given number
# Greedy approach would be to finish 3 tasks at every round until it is no
# longer possible then finish 2 rounds at every round, will require backtracking
# Time complexity O(n+m)


class Solution:
    # Approach 1:
    def minimumrounds_DP(bruh, n, dic={}):
        if n == 2 or n == 3:
            return 1
        if n <= 1:
            return -1
        if dic.get(n) is not None:
            return dic[n]
        ways = bruh.minimumrounds_DP(n - 2, dic) + 1
        ways2 = bruh.minimumrounds_DP(n - 3, dic) + 1

        if ways == 0:
            ways = 9999999999
        if ways2 == 0:
            ways2 = 9999999999
        dic[n] = min(ways, ways2)

        return dic[n]

    # Approach 2:
    # TODO: finsih this
    def minimumrounds_Greedy(bruh, n):
        pass
        # res = 0
        # for i in range(len(n)):

        #     if n[i] % 3 == 0:
        #         res += n[i] // 3
        #         continue

        #     elif n[i] % 3 == 1:
        #         res += ((n[i] - 4) // 3) + 2
        #         continue

        #     else:
        #         res += n[i] // 2
        # return res


sol = Solution()
ls = [14, 6, 12]
s = 0
for i in ls:
    s += sol.minimumrounds_DP(i)
print(s, sol.minimumrounds_Greedy(ls))
