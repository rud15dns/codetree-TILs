# 1. len(a) 
n = int(input())

arr = list(map(int, input().split()))

avg_cnt = 0
for i in range(n):
    for j in range(i, n):
        sum_arr = 0
        cnt = j + 1 - i
        for k in range(i, j + 1):
            sum_arr += arr[k]
        
        if sum_arr % cnt == 0 and (sum_arr / cnt) in arr[i: j+1]:
            #print(i, j, sum_arr / cnt)
            avg_cnt += 1

print(avg_cnt)