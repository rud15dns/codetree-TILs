import sys
INT_MAX = sys.maxsize

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

min_dist = INT_MAX
for i in range(1, n-1):
    distance = 0
    prev = 0

    for j in range(1, n):
        if j == i:
            continue
        distance += abs(arr[prev][0] - arr[j][0]) + abs(arr[prev][1] - arr[j][1])
        prev = j
    
    min_dist = min(min_dist, distance)

print(min_dist)