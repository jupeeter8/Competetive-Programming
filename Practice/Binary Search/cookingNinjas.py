def isPossible(rank: list[int], m: int, mid: int) -> bool:
    time = 0
    dishes = 0
    i = 0
    mul = 1
    while i < len(rank):
        if time + mul * rank[i] <= mid:
            time = time + mul * rank[i]
            dishes += 1
            if dishes == m:
                return True
            mul += 1
        else:
            i += 1
            mul = 1
            time = 0
    return False


def cookingNinja(rank: list[int], m: int) -> int:
    s = 0
    # rank.sort()
    ma = max(rank)
    e = int((m / 2) * ((2 * ma) + ((m - 1) * ma)))
    ans = -1
    while s <= e:
        mid = (s + e) // 2

        if isPossible(rank, m, mid):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    return ans


ranks = [1, 2, 3, 4]
m = 11
print(cookingNinja(ranks, m))
