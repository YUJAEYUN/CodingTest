arr = input()
n = int(input())
arr = arr[::-1]
for i in range(n):
    if n > len(arr):
        print(arr[::-1])
        break
    print(arr[i], end="")
