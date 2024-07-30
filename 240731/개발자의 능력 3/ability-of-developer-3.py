min_diff = 1000000 * 3
n = 6

arr = list(map(int, input().split()))


def get_diff(i, j, k):
    sum1 = arr[i] + arr[j] + arr[k]
    sum2 = sum(arr) - sum1
    
    return abs(sum1 - sum2)


for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            min_diff = min(min_diff, get_diff(i, j, k))

print(min_diff)