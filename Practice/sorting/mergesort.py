import random


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # Create Left and Right subarry
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        # Comparing 1st element of left and right subarry and copying the
        # Smaller to arr
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copying the remaining array to arr
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# crate a random array of size 100
arr = [random.randint(1, 100) for i in range(10)]
mergeSort(arr)
print(arr)
