def binaryToDecimal(n: int) -> int:
    i = 0
    answer = 0
    while n > 0:
        answer = answer + ((n & 1) * (2**i))
        n = n >> 1
        i += 1
    return answer


if __name__ == "__main__":
    n = int(input(), 2)
    print(binaryToDecimal(n))
