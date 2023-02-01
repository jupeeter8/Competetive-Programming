from typing import List


def equilibriumPoint(A: List[int], N: int) -> int:
    sum1 = 0
    sum2 = 0
    i = 0
    j = N - 1

    while i <= j:
        if sum1 == sum2 and i == j:
            return i
        elif sum1 == sum2 and i != j:
            sum1 = sum1 + A[i]
            i += 1
        elif sum1 > sum2:
            sum2 = sum2 + A[j]
            j -= 1
        elif sum1 < sum2:
            sum1 = sum1 + A[i]
            i += 1
    return -1


def main():
    array = [1, 3, 5, 2, 2]
    pos = equilibriumPoint(array, len(array))
    print(pos)


main()
