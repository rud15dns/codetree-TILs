n, m = tuple(map(int, input().split()))

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

arr = [
    list(input())
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


cnt = 0 
for i in range(n):
    for j in range(m):
        if arr[i][j] != "L":
            continue
        
        for dx, dy in zip(dxs, dys):
            curt = 1
            curx = i
            cury = j

            while True:
                nx = curx + dx
                ny = cury + dy

                if not in_range(nx, ny):
                    break
                if arr[nx][ny] != "E":
                    break
                if curt == 3:
                    break

                curt += 1
                curx = nx
                cury = ny
                #print(curx, cury)

            if curt == 3:
                #print(curx, cury)
                cnt += 1
                

print(cnt)