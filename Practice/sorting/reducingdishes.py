import random


def reduceDishes(sat: list[int]) -> int:
    # Fucntion Checks for total satisfaction using every suffix
    sat.sort()
    satisfaction = 0
    for i in range(len(sat)):
        mul = 1
        curr_satisfaction = 0
        for j in range(i, len(sat)):
            curr_satisfaction = curr_satisfaction + sat[j] * mul
            mul += 1
        satisfaction = max(curr_satisfaction, satisfaction)
    return satisfaction


def reduceDishes2(sat: list[int]) -> int:
    sat.sort()
    satisfaction = 0
    total_satisfation = 0
    prefix_sum = 0

    for i in reversed(range(len(sat))):
        prefix_sum += sat[i]
        total_satisfation += prefix_sum
        satisfaction = max(satisfaction, total_satisfation)
    return satisfaction


sat = [random.randint(-100, 100) for i in range(10000)]
# print(reduceDishes(sat))
print(reduceDishes2(sat))
