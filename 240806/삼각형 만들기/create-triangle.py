# 직각삼각형 => 세 개의 점 중 두 개의 점이 y좌표가 같고, 그 두 개의 점 중에서 하나의 점만 x좌표가 같다.
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_area = -1


def triangle(i, j, k):
    x1, y1 = arr[i]
    x2, y2 = arr[j]
    x3, y3 = arr[k]


    if y1 == y2 and y2 == y3 and y1 == y3:
        return -1
    if y1 != y2 and y2 != y3 and y1 != y3:
        return -1
    
    #y중에서 두 개는 같음. (x축 평행)

    if y1 == y2:
        if x1 == x3:
            return abs(y3 - y1) * abs(x3 - x2)
        if x2 == x3:
            return abs(y3 - y2) * abs(x3 - x1)
    if y2 == y3:
        if x2 == x1:
            return abs(y1 - y2) * abs(x1 - x3)
        if x3 == x1:
            return abs(y1 - y3) * abs(x1 - x2)
    if y1 == y3:
        if x1 == x2:
            return abs(y2 - y1) * abs(x2 - x3)
        if x3 == x2:
            return abs(y2 - y3) * abs(x2 - x1)
    return -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            area = triangle(i, j, k)
            #print(area)
            max_area = max(max_area, area)
            #print(max_area)

print(max_area)