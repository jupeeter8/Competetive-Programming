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
    # create a sorted rotated array of 200 elements
    arr = [i + 1 for i in range(200)]
    # rorate the array by 35 elements
    arr = arr[35:] + arr[:35]
    n = len(arr)
    print(arr)
    print(findPiviotElement(arr, 0, n - 1))


main()
