arr = [input().split() for j in range(7)]

result = [[0 for i in range(3)] for j in range(3)]

for i in range(3):
    for j in range(3):
        result[i][j] = (int(arr[i][j])*int(arr[i+4][j]))

for result in result:
    print(*result)