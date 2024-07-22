max_val = 0
a = list(input())
for i in range(len(a)):
    a[i] = int(a[i])

for i in range(len(a)):
    sum_max = 0
    a[i] = abs(1 - a[i])

    for j in range(len(a)):
        sum_max += a[j] * (2 ** (len(a) - j -1))

    max_val = max(sum_max, max_val)
    a[i] = abs(1 - a[i])

print(max_val)