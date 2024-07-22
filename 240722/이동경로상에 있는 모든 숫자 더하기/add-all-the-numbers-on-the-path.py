n, t = tuple(map(int, input().split()))
direction = list(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

x, y = n // 2, n // 2
total = arr[x][y]

start_num = 1
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


for elem in direction:
    if elem == "R":
        start_num = (start_num + 3) % 4
    elif elem == "L":
        start_num = (start_num + 1) % 4
    else: #"F"
        nx = x + dx[start_num]
        ny = y + dy[start_num]
        if not in_range(nx, ny):
            continue

        x = x + dx[start_num]
        y = y + dy[start_num]
        total = total + arr[x][y]

    #print(elem, x, y, start_num, total)
print(total)