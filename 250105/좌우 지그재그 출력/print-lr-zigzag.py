n = int(input())
cnt = 1

for i in range(n):
    for j in range(n):
        if i%2==0 and j==0:
            cnt = i*n +1
            print(cnt, end =" ")
            cnt+=1
        elif i%2==0:
            print(cnt, end=" ")
            cnt+=1
            
        elif i%2!=0 and j==0:
            cnt = (i+1)*n
            print(cnt, end =" ")
            cnt-=1
        elif i%2!=0:
            print(cnt, end=" ")
            cnt-=1
    print()