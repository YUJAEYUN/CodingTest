m = int(input())

for i in range(m):
    cnt=0
    n = int(input())
    while n != 1:
        if n%2==0:
            n/=2
            cnt+=1
        else:
            n=n*3+1
            cnt+=1
    print(cnt)