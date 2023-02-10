from typing import List


def twosCompliment(a: List[int]) -> List[int]:
    carry = 1
    for idx, bit in enumerate(a):
        if carry == 0:
            return a[::-1]
        if bit == 1:
            if carry == 0:
                return a[::-1]
            carry = 1
            a[idx] = 0
        else:
            if carry == 0:
                return a[::-1]
            carry = 0
            a[idx] = 1
    return a[::-1]


def negToBinary(n: int) -> int:
    if n >= 0:
        return None

    n = abs(n)
    b = ~n
    bit_arr = []
    while n > 0:
        bit_arr.append(b & 1)
        n = n >> 1
        b = b >> 1
    bit_arr = twosCompliment(bit_arr)
    return bit_arr


def main():
    n = int(input("> Enter a number "))
    print(negToBinary(n))


main()
