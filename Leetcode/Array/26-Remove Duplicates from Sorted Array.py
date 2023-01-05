from typing import List

# LC 26: Remove Duplicates from sorted Array

# Given a sorted list, remove duplicate elements. Since size of the list can
# not be changed, if k duplicates are removed then the first n-k positions of
# the list should have the remaning elements

# Approach 1: Since the list is sorted duplicate elements will be next to each
# other, with this idea we can check if a[i-1] == a[i]
# and set a[i-1] to max(a) + 1 after 1 pass, all duplicates will be
# set to max(a) + 1 we can then sort the array to send all max(a) +1 elements
# to the end
# Time complexity: O(n) + O(nlogn) -> O(nlogn)

# Appraoch 2: Using Fast and Slow pointer
# TODO: Implement fast and slow


class Solution:
    # Approach 1:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = max(nums) + 1
        k = n
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                nums[i - 1] = l
                k -= 1
        nums.sort()

        return k


def main():

    sol = Solution()
    print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


main()
