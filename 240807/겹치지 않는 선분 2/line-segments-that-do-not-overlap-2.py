n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

sorted_points = sorted(points)
cnt = 0

for i in range(n):
    x1, x2 = sorted_points[i]
    duplicate = False
    for j in range(n):
        if i == j:
            continue
        xx1, xx2 = sorted_points[j]

        # 겹치는 경우를 판별
        if not (x2 < xx1 or xx2 < x1):
            duplicate = True
            break  # 이미 겹치는 선분을 찾았으므로 더 이상 검사할 필요 없음

    if duplicate:
        cnt += 1

print(n - cnt)