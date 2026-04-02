N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
ans = 0

for i in range(N):
    tmp = 0
    cnt = 0
    for j in range(N):
        if tmp < B:
            cnt +=1
            if i == j:
                tmp += P[j]//2
            else:
                tmp += P[j]
        if tmp > B:
            cnt-=1
    ans = max(ans,cnt)
print(ans)