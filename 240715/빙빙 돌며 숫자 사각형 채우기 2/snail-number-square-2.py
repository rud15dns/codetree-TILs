n, m = tuple(map(int, input().split()))

arr = [
    [0] * m
    for _ in range(n)
]

x, y = 0, 0
start_dir = 0

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
def inrange(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


arr[x][y] = 1
for i in range(2, n * m + 1):
    nx, ny = x + dxs[start_dir], y + dys[start_dir]

    if not inrange(nx, ny) or arr[nx][ny] != 0:
        start_dir = (start_dir + 1) % 4
    
    x = x + dxs[start_dir]
    y = y + dys[start_dir]
    
    arr[x][y] = i
    

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()