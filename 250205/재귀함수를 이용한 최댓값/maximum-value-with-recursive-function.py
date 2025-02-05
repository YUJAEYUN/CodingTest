n = int(input())
arr = list(map(int, input().split()))
maximum = 0
# Write your code here!
def recursive(n):
    global maximum, arr
    
    if n == 0:
        return n if n == maximum else maximum
    elif arr[n-1] > maximum:
        maximum = arr[n-1]
        return recursive(n-1)
    return recursive(n-1)


print(recursive(n))