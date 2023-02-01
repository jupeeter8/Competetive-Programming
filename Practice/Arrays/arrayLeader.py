class Solution:
    def leaders(self, A, N):
        leader = []
        curr_leader = -1

        for i in reversed(range(N)):
            if A[i] >= curr_leader:
                leader.append(A[i])
                curr_leader = A[i]

        return leader[::-1]


def main():
    sol = Solution()
    A = [16, 17, 4, 3, 5, 2]
    N = len(A)

    print(sol.leaders(A, N))


main()
