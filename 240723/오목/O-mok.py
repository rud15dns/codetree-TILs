arr = [
    list(map(int, input().split()))
    for _ in range(19)
]

def in_range(x, y):
    return 0 <= x and x < 19 and 0 <= y and y < 19


def down(x, y, stand):
    for i in range(5):
        if stand != arr[x + i][y] or in_range(x + i, y) == False:
            return 0, 0, False
    return x + 2, y, True


def left(x, y, stand):
    for i in range(5):
        if stand != arr[x][y + i] or in_range(x, y + i) == False:
            return 0, 0, False
    return x, y + 2, True


def diagonal(x, y, stand):
    for i in range(5):
        if stand != arr[x + i][y + i] or in_range(x + i, y + i) == False:
            return 0, 0, False
    return x + 2, y + 2, True


for i in range(19):
    result = False
    for j in range(19):
        if arr[i][j] == 0:
            continue
        stand = arr[i][j]
        x, y, result = down(i, j, stand)
        if not result:
            x, y, result = left(i, j, stand)
        if not result:
            x, y, result = diagonal(i, j, stand)
        
        if result:
            break
    if result:
        print(stand)
        print(x + 1, y + 1)
        break