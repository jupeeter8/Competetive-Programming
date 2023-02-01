from typing import List, Tuple


class Solution:
    def swap(self, x: int, y: int) -> Tuple[int, int]:
        x, y = y, x

        return (x, y)

    def twopointer(self, array: List[int], n: int) -> List[int]:
        l: int = 0
        h: int = n - 1

        while l <= h:
            if array[l] == 0:
                l += 1
            if array[l] == 1:
                array[l], array[h] = self.swap(array[l], array[h])
                h -= 1
        return array


def main():

    sol = Solution()

    array = [0, 1, 1, 0, 1, 0, 0]

    print(sol.twopointer(array, len(array)))


main()
