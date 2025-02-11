
n = int(input())
sequence = list(map(int, input().split()))
li = [0 for _ in range(n)]
# Write your code here!
idx = 0
cnt=1
for j in range(n):
    minimum = 1000001
    for i in range(n):
        if sequence[i]<minimum:
            idx = i
            minimum = sequence[i]
    sequence[idx] = 1000001
    li[idx] = cnt
    cnt+=1
        
print(*li)

