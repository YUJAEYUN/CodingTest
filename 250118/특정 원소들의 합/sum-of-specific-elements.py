arr = []
for i in range(4):
    temp = list(map(int,input().split()))
    arr.append(temp)
result = 0

for i in range(4):
    for j in range(i+1):
        result += arr[i][j]
print(result)
