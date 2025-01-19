n = int(input())

arr = [[0 for i in range(n)] for j in range(n)]

cnt = 1

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if n%2!=0: # n이 홀수
            if i%2!=0:
                arr[n-1-j][i] = cnt
                cnt+=1
            
            else:
                arr[j][i] = cnt
                cnt+=1
        else: #n이 짝수
            if i%2==0:
                arr[n-1-j][i] = cnt
                cnt+=1
            
            else:
                arr[j][i] = cnt
                cnt+=1
        
for arr in arr:
    print(*arr)