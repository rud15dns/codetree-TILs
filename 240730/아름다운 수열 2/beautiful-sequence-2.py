n, m = tuple(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

k = len(b)
cnt = 0
b.sort()

for i in range(n - k + 1):
    arr_1 = a[i:i+k]
    
    arr_1.sort()
    #print(arr_1, b)
    if (arr_1 == b):
    #    print(arr_1, b)
        cnt += 1
#    arr_1.sort() == b.sort()

print(cnt)