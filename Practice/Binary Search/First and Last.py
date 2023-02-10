from typing import List, Tuple


def findFirstAndLast(arr: List[int], idx: int, n: int) -> Tuple[int, int]:
    first = idx
    last = idx
    ff = False
    fl = False

    while not ff or not fl:
        if first - 1 >= 0 and arr[first - 1] != arr[idx]:
            ff = True
        elif first - 1 >= 0:
            first = first - 1
        else:
            ff = True

        if last + 1 <= n - 1 and arr[last + 1] != arr[idx]:
            fl = True
        elif last + 1 <= n - 1:
            last = last + 1
        else:
            fl = True
    return (first, last)


def binarySearch(arr: List[int], l: int, h: int, key: int) -> int:
    mid = (l + h) // 2
    if l > h:
        return -1
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binarySearch(arr, mid + 1, h, key)
    else:
        return binarySearch(arr, l, mid - 1, key)


def main():

    n = 25
    # make a sorted array of size n with some duplicates
    arr = [i // 2 for i in range(n)]
    print(arr)
    key = 11
    idx = binarySearch(arr, 0, n - 1, key)
    print(findFirstAndLast(arr, idx, n))


main()
