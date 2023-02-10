from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    l = 0
    h = len(arr) - 1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid
        elif arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            h = mid - 1


def peakIndexInMountainArray2(arr: List[int]) -> int:
    l = 0
    h = len(arr) - 1

    while l < h:
        mid = (l + h) // 2
        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            h = mid
    return l


def main():
    arr = [0, 1, 2, 3, 1, 0]
    print(peakIndexInMountainArray2(arr))


main()
