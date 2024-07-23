arr = [
    list(map(int, input().split()))
    for _ in range(19)
]

def in_range(x, y):
    return 0 <= x and x < 19 and 0 <= y and y < 19


def down(x, y, stand):
    for i in range(5):
        if not in_range(x + i, y) or stand != arr[x + i][y]:
            return 0, 0, False
    return x + 2, y, True


def left(x, y, stand):
    for i in range(5):
        if not in_range(x, y + i) or stand != arr[x][y + i]:
            return 0, 0, False
    return x, y + 2, True


def diagonal_left(x, y, stand):
    for i in range(5):
        if not in_range(x + i, y - i) or stand != arr[x + i][y - i]:
            return 0,0,False
    return x + 2, y - 2, True

def diagonal_right(x, y, stand):
    for i in range(5):
        if not in_range(x + i, y + i) or stand != arr[x + i][y + i]:
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
            x, y, result = diagonal_left(i, j, stand)
        if not result:
            x, y, result = diagonal_right(i, j, stand)
        
        if result:
            break
        #print(i, j)
        

    if result:
        print(stand)
        print(x + 1, y + 1)
        break