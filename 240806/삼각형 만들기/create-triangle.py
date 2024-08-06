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

##어차피 세개 다 같으면 max값이 될 수 없음을 이용(해설 참고)
#def area(x1, y1, x2, y2, x3, y3):
#    return abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3))

#for i in range(n):
#    for j in range(i + 1, n):
#        for k in range(j + 1, n):
#            x1, y1 = arr[i]
#            x2, y2 = arr[j]
#            x3, y3 = arr[k]
            #처음에는 꼭 두개가 같아야 하는 시나리오가 있다고 생각하였으나.
            # 두 가지 조건 중에 하나씩 하나씩만 만족해도 무조건 최소 직각삼각형이 발생할 수밖에 없음.
#            if (x1 == x2 or x2 == x3 or x1 == x3) and (y1 == y2 or y2 == y3 or y1 == y3):
#                max_area = max(max_area, area(x1, y1, x2, y2, x3, y3))