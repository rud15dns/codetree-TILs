import sys
sum_diff = sys.maxsize

n = 5
arr = list(map(int, input().split()))

def sum_op(i, j, k):
    sum1 = arr[i]
    sum2 = arr[j] + arr[k]
    sum3 = sum(arr) - (sum1 + sum2)

    
    if (sum1 == sum2) or (sum2 == sum3) or (sum1 == sum3):
        return -1

    #print(i, j,k, sum1, sum2, sum3, "\t", max(sum1, sum2, sum3), min(sum1, sum2, sum3))
    return max(sum1, sum2, sum3) - min(sum1, sum2, sum3)


for i in range(n):
    for j in range(i + 1, n):
        for k in range(n):
            if k == i or k == j:
                continue
            
            min_sum = sum_op(k, i, j)
            if min_sum < 0:
                continue
                
            sum_diff = min(sum_diff, min_sum)
            #print(i, j, k, sum_diff)

if sum_diff == sys.maxsize:
    print(-1)
else:
    print(sum_diff)