n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
def div_even(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i]//=2
    print(*arr)

div_even(arr)
