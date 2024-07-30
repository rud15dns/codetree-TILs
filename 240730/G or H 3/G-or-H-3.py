MAX_NUM = 10000
n, k = tuple(map(int, input().split()))

arr = [0] * (MAX_NUM + 1)

for i in range(n):
    num, alpha = input().split()
    if alpha == 'G':
        arr[int(num)] = 1
    else:
        arr[int(num)] = 2

print(arr[:17])
max_cnt = 0
for i in range(1, MAX_NUM + 1 - k):
    num_cnt = 0
    for j in range(i, i + k):
        num_cnt += arr[j]
    
    max_cnt = max(num_cnt, max_cnt)

print(max_cnt)