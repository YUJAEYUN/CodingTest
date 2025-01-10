arr = input().split()
cnt=0
for i in range(len(arr)):
    if arr[i] == "0":
        arr.pop()
        print(*arr[::-1])
    cnt+=1
    if cnt == len(arr):
        print(*arr[::-1])
