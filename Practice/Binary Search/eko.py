from typing import List


def isPossible(tress: List[int], m: int, mid: int) -> bool:
    cut_m = 0

    for i in range(len(trees)):
        if trees[i] > mid:
            cut_m += trees[i] - mid
        if cut_m >= m:
            return True
    return False


def eko(trees: List[int], m: int) -> int:
    trees.sort()
    s = 0
    e = trees[-1]
    ans = -1
    while s <= e:
        mid = (s + e) // 2
        if isPossible(trees, m, mid):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans


n, m = tuple(map(int, input().split()))
trees = list(map(int, input().split()))
print(eko(trees=trees, m=m))
