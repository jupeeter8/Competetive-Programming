def decToBinary(n: int) -> int:
    """
    Converts a base 10 digit to base 2 by repetadly dividing by 2
    """
    answer = 0
    i = 0
    while n > 0:
        bit = n % 2
        n = n // 2
        answer = (bit * (10**i)) + answer
        i += 1
    return answer


def decToBinaryBit(n: int) -> int:
    """
    Converts a base 10 digit to base 2 by repeteadly right shifting
    """

    answer = 0
    i = 0
    while n > 0:
        bit = n & 1
        n = n >> 1
        answer = (bit * (10**i)) + answer
        i += 1
    return answer


if __name__ == "__main__":
    n = 20
    print(decToBinary(n))
    print(decToBinaryBit(n))

    assert decToBinary(n) == decToBinaryBit(2), "nice"
