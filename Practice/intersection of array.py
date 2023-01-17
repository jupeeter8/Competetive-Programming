# Given two sorted array find the intersection of the two arrays


def intersection(arr, brr, n, m):

    i = 0
    j = 0

    res = []

    while True:
        if i == n or j == m:
            break

        if arr[i] == brr[j]:
            res.append(arr[i])
            i += 1
            j += 1
        elif arr[i] < brr[j]:
            i += 1
        else:
            j += 1

    return res if res else -1


def main():

    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(intersection(a, b, n, m))


main()
