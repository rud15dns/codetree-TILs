n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = 0

for i in range(n - k + 1):
    total = 0
    for j in range(i, i + k):
        total += arr[j] 
    
    max_sum = max(total, max_sum)

print(max_sum)