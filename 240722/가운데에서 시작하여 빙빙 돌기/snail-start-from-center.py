#1차 접근 : 11, 22, 33, 44, 4 이런 식으로 변의 길이를 늘려나가기 
#2차 접근 : 25 부터 시작해서 1까지 거꾸로 계산해보기 
n = int(input())
arr = [
    [0] * n 
    for _ in range(n)
]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

start_num = 0
x, y = n-1, n-1
arr[x][y] = n * n


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


for i in range(n * n - 1, 0, -1):
    nx = x + dx[start_num]
    ny = y + dy[start_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        start_num = (start_num + 1) % 4
    
    x = x + dx[start_num]
    y = y + dy[start_num]
    arr[x][y] = i

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()