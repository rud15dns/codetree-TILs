#1. 첫번째 조합과의 거리가 2이내
#2. 두번째 조합과 거리가 2 이내
n = int(input())
a1, b1, c1 = tuple(map(int, input().split()))
a2, b2, c2 = tuple(map(int, input().split()))


def first_distance(i, j, k):
    return (abs(i - a1) <= 2 or abs(a1 - i) >= n -2) and \
    (abs(j - b1) <= 2 or abs(b1 - j) >= n - 2) and \
    (abs(k - c1) <= 2 or abs(c1 - k) >= n - 2)


def second_distance(i, j, k):
    return (abs(i - a2) <= 2 or abs(a2 - i) >= n - 2) and \
    (abs(j - b2) <= 2 or abs(b2 - j) >= n - 2) and \
    (abs(k - c2) <= 2 or abs(c2 - k) >= n - 2)


cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if first_distance(i, j, k) or second_distance(i, j, k):
                cnt += 1

print(cnt)