import sys
n, h, t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

cnt_min = sys.maxsize

for i in range(n):
    for j in range(i, n):
        sum_min = 0
        for k in range(i, j + 1):
            sum_min += abs(h - arr[k])
        #    print(sum_min)
            
        if (j + 1 - i) >= t:
            cnt_min = min(sum_min, cnt_min)

        #print()

print(cnt_min)