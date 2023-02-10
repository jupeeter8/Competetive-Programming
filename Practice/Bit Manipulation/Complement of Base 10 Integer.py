# 1009 Complement of Base 10 Integer
# Given a base 10 ineteger find it's complement


class Solution:
    def base10bitwiseComplement(self, num: int) -> int:
        if num == 0:
            return 1
        # Negating the number will filp all the bits of the number
        # This will cause the actual bits to be flipped but we need
        # only the bits that were present in the in actual number

        # let's say integers are stored using 8 bits
        # 5 will be stored as 00000101. ~5 will be
        # 11111010. we are only interested in the bits to the right of MSB
        # in the actual number
        # 00000(101) : Part we are interesetd in
        # 11111(010) : 010 in binary is 2 which is complment of 101 i.e. 5
        # We can left shift n until it becomes zero and store &1 of the
        # lsb in ~5 since bit & 1 produces itself
        b = ~num
        binary = ""
        while num:
            binary = str(b & 1) + binary
            num = num >> 1
            b = b >> 1
        return int(binary, 2)


def main():
    sol = Solution()

    n = 5
    print(sol.base10bitwiseComplement(n))


main()
