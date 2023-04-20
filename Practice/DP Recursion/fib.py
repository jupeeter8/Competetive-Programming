import random


def fib(n: int, memo={}):

    if n <= 2:
        return 1
    elif memo.get(n) is None:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]
    else:
        return memo[n]


if __name__ == "__main__":
    print(fib(120))
