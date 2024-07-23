import sys
sum_max = -sys.maxsize

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 2, n):
        summ = a[i] + a[j]
        sum_max = max(summ, sum_max)
        #print(sum_max)

print(sum_max)