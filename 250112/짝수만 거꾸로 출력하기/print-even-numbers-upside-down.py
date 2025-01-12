n = int(input())

arr = input().split()

for i in range(len(arr)-1,-1, -1):
    if int(arr[i])%2==0:
        print(arr[i], end=" ")