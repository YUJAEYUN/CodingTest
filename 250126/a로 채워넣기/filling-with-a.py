arr = list(input())
arr[1] = 'a'
arr[-2] = 'a'
for i in range(len(arr)):
    print(arr[i],end="")