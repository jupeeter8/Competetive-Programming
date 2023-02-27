def findPiviotElement(arr, l, h):
    mid = (l + h) // 2
    if l > h:
        return -1
    elif arr[mid] < arr[mid - 1]:
        return arr[mid]
    elif arr[mid] < arr[l]:
        return findPiviotElement(arr, l, mid - 1)
    else:
        return findPiviotElement(arr, mid + 1, h)


def main():
    # create a sorted rotated array
    arr = [5, 6, 7, 8, 9, 21, 2, 3]
    n = len(arr)
    print(findPiviotElement(arr, 0, n - 1))


main()
