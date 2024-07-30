MAX_INT = 100
n, k = tuple(map(int, input().split()))

arr = [0] * (MAX_INT + 1)
for i in range(n):
    num, direc = tuple(map(int, input().split()))
    arr[direc] += num

#print(arr[:16])
sum_max = 0


for i in range(1, MAX_INT + 1):
    sum_candy = 0
    if i + 2 * k + 1 > MAX_INT:
        l = MAX_INT
    else:
        l = i + 2 * k
    for j in range(i, l + 1):
        #print(j, end = ' ')
        sum_candy += arr[j]

    #print()
    sum_max = max(sum_candy, sum_max)


print(sum_max)