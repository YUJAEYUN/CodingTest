n = int(input())
arr = list(map(int, input().split()))
res = []
# Write your code here!
for i in range(n):
    res.append(arr[i])
    if i%2==0:
        res.sort()
        print(f"{res[(i+1)//2]}", end=" ")