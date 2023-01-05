# 217. Contains Duplicate
# Given an array, return True if array contains a Duplicate, False if all
# Elements are distinct

# Approach 1: We can use brute force to check if there is a similar
# element using 2 loops Time Complexity will be O(n^2)

# Approach 2: We can sort the array and check adjecnt values
# Time Complexity will be O(nLog(n))

# Approach 3: We can use a hashmap like data structure
# To keep trak of elements we have visited. In python
# We can use a dictionary to achive this
# Time complexity will be O(n)

# Appraoch 4: Creating A hashtable of size max(arrray) - min(array) + 1
# This will allow us to index negative elements but will fail for large
# Values of array[i]. Time complexity: O(n)

from typing import List


class Solution:
    # Approach 4:
    def containsDuplicate(self, nums: List[int]) -> bool:

        mi = nums[0]
        ma = nums[0]
        n = len(nums)
        for i in range(n):
            mi = min(mi, nums[i])
            ma = max(ma, nums[i])

        if mi < 0:
            size = (ma - mi) + 1
            start = abs(mi)
        else:
            size = ma + 1
            start = 0
        array = [0] * size

        for i in range(n):
            # print(start+nums[i])
            if array[start + nums[i]] == 1:
                return True
            array[start + nums[i]] = 1
        return False

    # Approach 3:
    def concontainsDuplicateHashmap(self, nums: List[int]) -> bool:
        visited = {}
        n = len(nums)
        for i in range(n):
            if visited.get(nums[i]) is not None:
                return True
            visited[nums[i]] = 1
        return False


sol = Solution()
res = sol.containsDuplicate([1, 2, 3, 1])
res2 = sol.concontainsDuplicateHashmap([1, 2, -1, 2, 0])
print(res, res2)
