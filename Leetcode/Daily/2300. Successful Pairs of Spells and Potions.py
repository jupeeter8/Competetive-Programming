def sol(spells: list[int], potions: list[int], success: int):
    slow = 0
    fast = len(potions) - 1
    spells_copy = spells[::]
    res = dict()
    spells.sort()
    potions.sort()
    while slow < len(spells) and fast > -1:
        if spells[slow] * potions[fast] >= success:
            fast -= 1
        else:
            res[spells[slow]] = len(potions) - (fast + 1)

            slow += 1

    while slow < len(spells):
        res[spells[slow]] = len(potions) - (fast + 1)
        slow += 1
    for i, val in enumerate(spells_copy):
        spells_copy[i] = res[val]
    return spells_copy


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]

print(sol(spells, potions, 7))
