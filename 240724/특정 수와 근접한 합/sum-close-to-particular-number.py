import sys
INT_MAX = sys.maxsize

n, s = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

min_sum = INT_MAX

for i in range(n):

    for j in range(i + 1, n):
        total = 0

        for k in range(n): #더할 것
            if k == i or k == j:
                continue
            total += arr[k]
        
        min_sum = min(abs(total - s), min_sum)
            
            
print(min_sum)