dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = tuple(map(int, input().split()))
arr = [
    [0] * m
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


start_num = 0
x, y = 0, 0

arr[x][y] = 'A'
for i in range(1, n * m):
    nx = x + dx[start_num]
    ny = y + dy[start_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        start_num = (start_num + 1) % 4
    
    x = x + dx[start_num]
    y = y + dy[start_num]

    arr[x][y] = chr(ord('A') + (i % 24))

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()