a = list(input())
n = len(a)
#print(a)

cnt = 0
for i in range(n - 1):
    if a[i] == a[i + 1] == "(":
        for j in range(i + 2, n - 1):
            if a[j] == a[j + 1] == ")": 
                cnt += 1

print(cnt)