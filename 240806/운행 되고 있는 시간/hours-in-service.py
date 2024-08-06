#적어도 한 명이 일하고 있으면 '운행 되고 있는 시간'
#그렇다면 전체 경우에서 아무도 일하지 않는 경우만,,,

#운행되고 있는 시간이 최대 -> 겹치지 않게 오래 

#문제 목표 : 최대한 선분이 안겹치도록 할 때의 sum(count)
max_count = 0

n = int(input())
people = [
    tuple(map(int, input().split())) 
    for _ in range(n)
]

for i in range(n):
    count = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        
        a, b = people[j]
        for k in range(a, b):
            count[k] = 1
    
    max_count = max(sum(count), max_count)

print(max_count)