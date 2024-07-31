min_sum = 40001 * 40001

n = int(input())

segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

for i in range(n):
    max_x = 0
    max_y = 0

    min_x = 40000 + 1
    min_y = 40000 + 1

    for j in range(n):
        if i == j:
            continue
        
        x, y = segments[j]

        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    
    #print(max_x, max_y, min_x, min_y)
    min_sum = min(min_sum, (max_x - min_x) * (max_y - min_y))

print(min_sum)