cnt = 0
n = int(input())
a = input()

for i in range(n): #C
    for j in range(i + 1, n): #O
        for k in range(j + 1, n): #W
            if a[i] == "C" and a[j] == "O" and a[k] == "W":
                cnt += 1

print(cnt)