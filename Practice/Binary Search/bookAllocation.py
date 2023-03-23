def isPossible(pages, n, m, mid):
    stud = 1
    page_sum = 0
    for i, page in enumerate(pages):
        if page_sum + page <= mid:
            page_sum = page_sum + page
        else:
            stud += 1
            if stud > m or page > mid:
                return False
            page_sum = page
    return True


def allocateBooks(pages, n, m):
    mi = 0
    ma = sum(pages)
    ans = -1

    while mi <= ma:
        mid = (mi + ma) // 2

        if isPossible(pages, n, m, mid):
            ans = mid
            ma = mid - 1
        else:
            mi = mid + 1
    return ans


def main():
    pages = [10, 20, 30, 40]
    n = 4
    m = 2

    print(allocateBooks(pages, n, m))


main()
