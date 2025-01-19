n = int(input())
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]


for j in range(n):
    arr_2d[j][0] = 1
    arr_2d[j][j] = 1


for i in range(1, n):
    for j in range(1, n):
        arr_2d[i][j] = arr_2d[i - 1][j-1] + arr_2d[i - 1][j]

# 출력
for row in arr_2d:
    for elem in row:
        if elem == 0:
            continue
        else:
            print(elem, end=" ")
    print()

