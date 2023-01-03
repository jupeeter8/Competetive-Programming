from typing import List

# 944. Delete Columns to Make Sorted
# Given A list of n length, lowercase strings, return
# the Number of columns that are not lexically sorted
# for Example: strs = ["abc", "bca", "cae"] then it can be looked at as a 2D
# strings:

#    c1 c2 c3
# r1 a  b  c
# r2 b  c  a
# r3 c  a  e

# We have to delete the columns that are not lexogrphically sorted that is c2

# Approach 1: Brute Force -> check all rows are greater then the previous one
# in a column using 2 For loops. Time Complexity O(n^2)


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0])
        rows = len(strs)

        d = 0
        for i in range(cols):
            for j in range(rows - 1):
                if not strs[j][i] <= strs[j + 1][i]:
                    d += 1
                    break
        return d


def main():
    sol = Solution()
    print(sol.minDeletionSize(["abc", "bca", "cae"]))


main()
