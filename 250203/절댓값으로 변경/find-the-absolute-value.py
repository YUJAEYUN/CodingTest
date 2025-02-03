n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
def absreturn(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    print(*arr)

absreturn(arr)