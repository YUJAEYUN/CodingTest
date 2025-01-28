arr = input()
n = len(arr)
print(arr)

for i in range(n):
    arr = arr[-1] + arr[0:n-1]
    print(arr)