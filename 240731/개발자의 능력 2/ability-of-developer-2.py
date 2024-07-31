import sys
sum_diff = sys.maxsize

arr = list(map(int, input().split()))
n = len(arr)

def sum_op(i, j, k, l):
    sum1 = arr[i] + arr[j]
    sum2 = arr[k] + arr[l]
    sum3 = sum(arr) - (sum1 + sum2)
    
    return max(sum1, sum2, sum3), min(sum1, sum2, sum3)


for i in range(n):
    for j in range(i + 1, n):
        for k in range(n):
            if k != i and k != j:
                for l in range(k + 1, n):
                    if l != j and l != i:
                        max_sum, min_sum = sum_op(i, j, k, l)
                        
                        #print(arr[i], arr[j], arr[k], arr[l])
                        sum_diff = min(abs(max_sum - min_sum), sum_diff)

print(sum_diff)