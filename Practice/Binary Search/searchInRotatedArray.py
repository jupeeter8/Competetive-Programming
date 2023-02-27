def findPivot(arr, l, h):
    mid = (l + h) // 2
    if l >= h:
        return l
    if arr[mid] >= arr[0]:
        return findPivot(arr, mid + 1, h)
    else:
        return findPivot(arr, l, mid)


def rotatedArraySearch(arr, l, h, key):
    mid = (l + h) // 2
    if l > h:
        return -1
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return rotatedArraySearch(arr, l, mid - 1, key)
    else:
        return rotatedArraySearch(arr, mid + 1, h, key)


def main():
    arr = [6, 9, 12, 15, 1, 2, 3, 5]
    pivotIdx = findPivot(arr, 0, len(arr) - 1)
    key = int(input())
    if arr[pivotIdx] <= key <= arr[-1]:
        print(rotatedArraySearch(arr, pivotIdx, len(arr) - 1, key))
    else:
        print(rotatedArraySearch(arr, 0, pivotIdx - 1, key))


main()
