n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
min_distance = 9999999

for i in range(1,n-1):
    point_x, point_y = 0,0
    distance = 0

    for j in range(1,n):
        if i == j:
            pass
        else:
            distance += abs(x[j]-x[point_x]) + abs(y[j] - y[point_y])
            point_x = j
            point_y = j
    min_distance = min(min_distance, distance)
print(min_distance)
