n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

result = -1

def carry(a, b, c):
    while True:
        
        #print("원래", a, b, c, end ='\t ')
        a_m = a % 10
        b_m = b % 10
        c_m = c % 10

        #print(a_m, b_m, c_m, a_m + b_m + c_m)
        if (a_m + b_m + c_m) >= 10:
            return False
        if a == 0 and b == 0 and c == 0:
            return True
        
        a = a // 10
        b = b // 10
        c = c // 10


max_sum = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if carry(arr[i], arr[j], arr[k]):
                #print(arr[i], arr[j], arr[k], carry(arr[i], arr[j], arr[k]))
                max_sum = max(max_sum, arr[i] + arr[j] + arr[k])
print(max_sum)