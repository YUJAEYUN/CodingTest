N = int(input())
a, b, c = map(int, input().split())
cnt=0
# Please write your code here.
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):

            if abs(a-i)<=2 or abs(b-j)<=2 or abs(c-k)<=2:
                cnt+=1

print(cnt)