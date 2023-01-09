# Practice problem
# Find Unique Elements in an Array of size N, array contains elements from 1 to
# N-1 with one duplicate element, find the duplicate element


def find_duplicate(array, N):

    total = (1 + N) * (N / 2)
    array_sum = sum(array)

    return int(N - (total - array_sum))


def main():
    N = int(input())
    array = list(map(int, input().split()))

    print(find_duplicate(array, N))


main()
