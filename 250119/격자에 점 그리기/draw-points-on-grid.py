n, m = map(int, input().split())
arr_2d = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    r, c = map(int, input().split())
    arr_2d[r-1][c-1] = i+1

for arr in arr_2d:
    print(*arr)
