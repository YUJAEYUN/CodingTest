arr = list(input())

for i in range(len(arr)):
    if arr[i] == 'e':
        arr.pop(i)
        break
arr = "".join(arr)
print(arr)