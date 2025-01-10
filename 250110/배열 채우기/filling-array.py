arr = input().split()
cnt=0
arr1 = []
for i in range(len(arr)):
    if arr[i] == "0":
        print(*arr1[::-1])
        break
    else:
        arr1.append(arr[i])
    cnt+=1
    if cnt == len(arr):
        print(*arr1[::-1])
