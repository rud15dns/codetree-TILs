#x1은 본인이 작은데, x2가 다른 선분이 작다면 -> 무조건 겹침.
n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

cnt = 0

for i in range(n):
    x1, x2 = points[i]
    for j in range(n):
        if i == j:
            continue
        xx1, xx2 = points[j]

        if x1 < xx1 and x2 > xx2:
            cnt += 2
    #print(cnt)

print(n - cnt)