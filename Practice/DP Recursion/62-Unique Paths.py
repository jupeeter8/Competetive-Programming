def uniquePaths(m,n, memo={}):
    if m == 1 or n == 1:
        return 1
    if memo.get((m, n)):
        return memo[(m, n)]
    if memo.get((n, m)):
        return memo[(n, m)]
    memo[(m, n)] = memo[(n, m)] = uniquePaths(m-1, n) + uniquePaths(m, n-1)
    return memo[(m, n)]

def uniquePaths2(m,n):
    dp = [[0 for _ in range(n)] for _ in  range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if dp[i][j] == 1:
                continue
            val1 = 0 if j -1 < 0 else dp[i][j-1]
            val2 = 0 if i -1 < 0 else dp[i-1][j]
            dp[i][j] = val1 + val2
    return dp[-1][-1]
             


print(uniquePaths2(3, 7))