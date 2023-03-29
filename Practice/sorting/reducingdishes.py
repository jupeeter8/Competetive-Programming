def reduceDishes(sat: list[int]) -> int:
    sat.sort()
    p = 0
    c = 0
    r = 0

    for i in reversed(range(len(sat))):
        p += sat[i]
        c += p
        r = max(r, c)
    return r


sat = [-1, -8, 0, 5, -7]
reduceDishes(sat)
