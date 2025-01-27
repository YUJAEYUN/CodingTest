arr = list(input())
tmp = arr[0]
res = arr[1]

for i in range(len(arr)):
    if arr[i]==res:
        arr[i] = tmp

for j in range(len(arr)):
    print(arr[j], end="")