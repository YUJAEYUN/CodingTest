n, m = map(int, input().split())

# Write your code here!
arr = [[0 for i in range(m)]for j in range(n)]
cnt=0

for i in range(m):
    for j in range(n):
        if i%2==0:
            arr[j][i] = cnt
            cnt+=1
        else:
            arr[n-j-1][i] = cnt
            cnt+=1

for arr in arr:
    print(*arr)