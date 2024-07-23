r, c = map(int, input().split())
arr = [
    list(input().split())
    for _ in range(r)
]

x, y = 0, 0
stand = arr[x][y]
cnt = 0
for i in range(1, r - 1):
    for j in range(1, c - 1):
        if arr[i][j] != stand:
            for k in range(i + 1, r - 1):
                for l in range(j + 1, c - 1):
                    if arr[k][l] == stand:
                        cnt += 1

print(cnt)