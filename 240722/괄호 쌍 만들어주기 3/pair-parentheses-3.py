a = list(input())
n = len(a)

cnt = 0
for i in range(n):
    if a[i] == '(':
        for j in range(i + 1, n):
            if a[j] == ')':
                cnt += 1

print(cnt)