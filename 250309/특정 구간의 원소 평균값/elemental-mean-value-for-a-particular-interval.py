n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0

for i in range(n): #시작점
    for j in range(i,n): #구간
        sum_val = 0
        cnt = 0
        for k in range(i,j+1):
            sum_val+=arr[k]
            cnt+=1
        avg = sum_val/cnt
        
        if avg in arr[i:j+1]:
            ans +=1
print(ans)