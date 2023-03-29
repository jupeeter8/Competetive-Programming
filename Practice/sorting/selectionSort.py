import random


def selection_sort(swap, array: list[int], n: int) -> None:
    for i in range(n):
        for j in range(i + 1, n):
            if array[j] < array[i]:
                array[i], array[j] = swap(array[i], array[j])


if __name__ == "__main__":
    array = [random.randint(0, 300) for _ in range(20)]
    print(array)
    n = 20
    selection_sort(swap=lambda x, y: (y, x), array=array, n=n)
    print(array)
