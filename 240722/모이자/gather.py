import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

min_val = INT_MAX
for i in range(n):
    sum_diff = 0 
    for j in range(n):
        sum_diff += arr[j] * (abs(j - i))

    #print(sum_diff)
    min_val = min(min_val, sum_diff)

print(min_val)