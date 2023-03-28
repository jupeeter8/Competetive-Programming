def isPossible(board: list[int], painter: int, mid: int) -> bool:
    boardPaint = 0
    k = 1
    for i in range(len(board)):
        if boardPaint + board[i] <= mid:
            boardPaint += board[i]
        else:
            boardPaint = board[i]
            k += 1
            if boardPaint > mid or k > painter:
                return False
    return True


def painterPart(board: list[int], painter: int) -> int:
    s = 0
    e = sum(board)
    ans = -1
    while s <= e:
        mid = (s + e) // 2
        if isPossible(board, painter, mid):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    return ans


arr = [1, 2, 3, 4]
k = 2

print(painterPart(arr, k))
