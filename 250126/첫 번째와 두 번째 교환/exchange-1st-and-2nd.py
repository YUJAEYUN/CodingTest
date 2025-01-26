arr = list(input())
tmp1 = arr[0]
tmp2 = arr[1]

for i in range(len(arr)):
    if arr[i] == tmp1:
        arr[i] = tmp2

    elif arr[i] == tmp2:
        arr[i] = tmp1

for j in range(len(arr)):
    print(arr[j],end="")