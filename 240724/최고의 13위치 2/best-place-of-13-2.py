n = int(input())
a = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
    

max_sum = 0

for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):
                l_m = l
                if i == k and in_range(k, j + 5):
                    l_m = l + j + 3
                elif i == k:
                    continue
                
                if not in_range(k, l_m + 2):
                    continue

                #print(i, j, i, j+1, i, j + 2, '\t', k, l_m, k, l_m+1, k, l_m +2)
                max_sum = max(max_sum, a[i][j] + a[i][j + 1] + a[i][j + 2] + a[k][l_m] + a[k][l_m + 1] + a[k][l_m + 2])

print(max_sum)