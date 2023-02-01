from typing import List, Tuple
import random


class Solution:
    def swap(self, x: int, y: int) -> Tuple[int, int]:
        x, y = y, x

        return (x, y)

    def twopointer(self, array: List[int], n: int) -> List[int]:
        l: int = 0
        h: int = n - 1

        while l < h:
            if array[l] == 0:
                l += 1
            if array[l] == 1:
                array[l], array[h] = self.swap(array[l], array[h])
                h -= 1
        return array


def makeArray() -> List[int]:
    val = [0, 1]
    n = random.randint(10, 10000)

    array = [random.choice(val) for i in range(n)]

    return array


def main():

    for i in range(100):
        sol = Solution()
        array = makeArray()
        new_array = sol.twopointer(array, len(array))
        print(i)
        # assert if the array is sorted
        assert new_array == sorted(array), print(new_array, array)


main()
