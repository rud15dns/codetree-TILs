import sys
min_val = sys.maxsize

n = int(input())
a = [
    int(input())
    for _ in range(n)
]


for i in range(n):
    dist = 0
    total = sum(a)
    for j in range(i, n):
        total -= a[j]
        dist += total 
    for j in range(0, i):
        total -= a[j]
        dist += total
    #print(dist)
    min_val = min(dist, min_val)

print(min_val)