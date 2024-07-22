n = int(input())
A = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if A[i] <= A[j] and A[j] <= A[k]:
                cnt += 1

print(cnt)