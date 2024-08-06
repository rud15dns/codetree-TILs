import sys

n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = sys.maxsize
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = arr[i]
        x2, y2 = arr[j]

        total = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        ans = min(ans, total)

print(ans)