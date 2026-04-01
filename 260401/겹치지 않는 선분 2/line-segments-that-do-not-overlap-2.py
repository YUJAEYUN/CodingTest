n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.

ans = 0

for i in range(n):
    tmp = 0    
    for j in range(n):
        if j == i:
            continue
        
        if not ((a[i] < a[j] and b[i] < b[j]) or (a[i] > a[j] and b[i] > b[j])):
            tmp+=1
    if tmp == 0:
        ans+=1
print(ans)
        