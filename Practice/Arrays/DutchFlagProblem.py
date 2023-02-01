from typing import List

# Sort 0s, 1s and 2s in a given array


class Solution:
    def sort012(self, array: List[int], n: int) -> List[int]:

        zeros = 0
        ones = 0

        for i in array:
            if not i:
                zeros += 1
            if i == 1:
                ones += 1

        for i in range(n):
            if i < zeros:
                array[i] = 0
            elif i < ones + zeros:
                array[i] = 1
            else:
                array[i] = 2

        return array

    def threePointer(self, array: List[int], n: int) -> List[int]:
        mid: int = 0
        lo: int = 0
        hi: int = n - 1

        while mid <= hi:
            if array[mid] == 1:
                mid = mid + 1

            elif array[mid] == 0:
                array[mid], array[lo] = array[lo], array[mid]
                lo = lo + 1
                mid = mid + 1

            elif array[mid] == 2:
                array[mid], array[hi] = array[hi], array[mid]
                hi = hi - 1
        return array


def main():
    sol = Solution()

    n = 9
    array = [0, 1, 1, 2, 0, 1, 0, 0, 2]

    print(sol.threePointer(array, n))


main()
