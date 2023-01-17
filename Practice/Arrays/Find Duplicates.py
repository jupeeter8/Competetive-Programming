# Practice problem
# Find Unique Elements in an Array of size N, array contains elements from 1 to
# N-1 with one duplicate element, find the duplicate element


def find_duplicate(array, N):

    total = (1 + (N - 1)) * ((N - 1) / 2)
    array_sum = sum(array)

    return int(array_sum - total)


def find_duplicate_xor(array, N):
    unique = 0
    for i in range(N):
        unique = unique ^ array[i]
        unique = unique ^ i
    return unique


def main():
    N = int(input())
    array = list(map(int, input().split()))

    print(find_duplicate(array, N))
    print(find_duplicate_xor(array, N))


main()
