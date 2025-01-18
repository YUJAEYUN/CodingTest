n, m = map(int,input().split())
arr1 = [input().split() for i in range(n)]
arr2 = [input().split() for i in range(n)]
result = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            result[i][j] = 0
        else:
            result[i][j] = 1

for result in result:
    print(*result)
