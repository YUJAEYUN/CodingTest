arr = list(map(int, input().split()))
n = len(arr)
numSum=0
for i in range(3, n):
    numSum = arr[i-1] + arr[i-2] + arr[i-3]
    if arr[i] == 0:
        print(numSum)
        break

