def isPossible(stalls: list[int], k: int, mid: int) -> bool:
    cows = 1
    prevCow = 0
    i = 0
    while i < len(stalls):
        if abs(stalls[prevCow] - stalls[i]) >= mid:
            prevCow = i
            cows += 1
        i += 1
    return cows >= k


def agressive_cows(stalls: list[int], k: int) -> int:
    s = 0
    e = max(stalls) - min(stalls)
    ans = -1
    stalls.sort()
    while s <= e:
        mid = (s + e) // 2
        if isPossible(stalls, k, mid):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans


stalls = [4, 2, 1, 3, 6]
k = 2

print(agressive_cows(stalls, k))
